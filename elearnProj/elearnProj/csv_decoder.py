import numpy as np
import pandas as pd
import regex as re
import matplotlib.pyplot as plt
from colorama import Fore, init

currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}

init(autoreset=True)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", "{:.2f}".format)


def get_amount(message, dataframe):
    print(Fore.LIGHTYELLOW_EX + message)
    result = dict()
    for key, value in dataframe:
        result[key] = value.__len__()
    return result


def get_salary(message, dataframe):
    print(Fore.LIGHTYELLOW_EX + message)
    result = dict()
    for key, value in dataframe:
        result[key] = value['rub_salary'].mean()
    return result


def get_salary_city(message, dataframe):
    result = get_salary(message, dataframe)
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True)[:10])


def get_amount_city(message, dataframe):
    result = get_amount(message, dataframe)
    sum = 0
    for values in result.values():
        sum += values
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True)[:9])
    result_proc = result
    other = 1
    for key, value in result_proc.items():
        result_proc[key] = value/sum
    for value in result_proc.values():
        other -= value
    result_proc['Другие'] = other
    return result, result_proc

def create_graph(keys, values, label, message, name, type):
    fig = plt.figure(figsize=(8, 8))
    width = 0.3
    x = np.arange(len(keys))
    ax = fig.add_subplot(plt.subplot(1, 1, 1))

    if type == "bar":
        rects = ax.bar(x - width / 2, values, width, label=label)
        ax.set_title(message, fontsize=20)
        ax.grid(axis='y')
        ax.set_xticks(x, fontsize=20)
        ax.set_xticklabels(keys, rotation=90, fontsize=20)
        ax.legend(loc='upper left', fontsize=15)
        plt.tick_params(axis='both', which='major', labelsize=15)
    elif type == "side":
        fig.set_size_inches(10, 10)
        ax.barh(keys, values)
        ax.grid(axis='x')
        plt.tick_params(axis='both', which='major', labelsize=11)
    elif type == "circle":
        ax.pie(values, labels=keys, radius=1.1, startangle=150)
        plt.rc('font', size=25)
    else:
        print(Fore.RED + "WRONG")

    fig.savefig('G:\djangoProject\elearnProj\demand\static\demand\images\\' + name + '.png', dpi=300)

def generate_image(salary_by_year, vac_by_year, salary_by_prof, vacancy_by_prof, salary_by_city, vacancy_by_city):
    cat_par_1 = list(salary_by_year.keys())
    year_val = list(salary_by_year.values())
    prof_val = list(salary_by_prof.values())
    year_vac = list(vac_by_year.values())
    prof_vac = list(vacancy_by_prof.values())
    cat_par_2 = list(salary_by_city.keys())
    sal_city = list(salary_by_city.values())
    cat_par_3 = list(vacancy_by_city.keys())
    vac_city = list(vacancy_by_city.values())

    create_graph(cat_par_1, year_val, 'Средняя з/п', 'Уровень зарплат по годам', 'Graph1', 'bar')
    create_graph(cat_par_1, prof_val, 'З/п GameDev', 'Уровень зарплат по годам', 'Graph2', 'bar')
    create_graph(cat_par_1, year_vac, 'Количество вакансий по годам', 'Количество вакансий', 'Graph3', 'bar')
    create_graph(cat_par_1, prof_vac, 'Количество вакансий по годам', 'Количество вакансий GameDev', 'Graph4', 'bar')
    create_graph(cat_par_2, sal_city, 'Заработная плата по городам', 'Заработная плата', 'Graph5', 'side')
    create_graph(cat_par_3, vac_city, 'Количество вакансий по городам', 'Количество вакансий', 'Graph6', 'circle')


if __name__ == '__main__':
    print(Fore.LIGHTGREEN_EX + 'Чтение CSV файла...')
    df = pd.read_csv('csv_files/vacancies_with_skills.csv')

    print(Fore.LIGHTGREEN_EX + 'Удаление лишних записей...')
    df = df.dropna()

    print(Fore.LIGHTGREEN_EX + 'Добавление столбцов...')
    df['year'] = df['published_at'].apply(lambda x: x[:4])
    df['mean_salary'] = df.loc[:, ['salary_to', 'salary_from']].mean(axis=1)
    df['koef'] = df['salary_currency'].apply(lambda x: currency_to_rub[x])
    df['rub_salary'] = df['mean_salary'] * df['koef']

    print(Fore.LIGHTGREEN_EX + 'Группировка данных...')
    df_group = df.groupby('year')

    salary_by_year = get_salary('Получение средней зароботной платы по годам...', df_group)
    vac_by_year = get_amount('Получение динамики вакансий по годам...', df_group)
    #print(vac_by_year)
    #print(salary_by_year)

    print(Fore.LIGHTGREEN_EX + 'Поиск вакансий с критериями...')
    df = df[df['name'].str.contains('game|gamedev|unity|unreal|\bигр', regex=True, flags=re.IGNORECASE)] #Поиск всех вакансий с игровыми названиями
    df_group = df.groupby('year')

    vacancy_by_prof = get_amount('Получение динамики вакансий GameDev по годам...', df_group)
    salary_by_prof = get_salary('Получение средней зароботной платы за год по вакансии GameDev...', df_group)
    #print(salary_by_prof)
    #print(vacancy_by_prof)

    print(Fore.LIGHTGREEN_EX + 'Группировка данных...')
    df_group = df.groupby('area_name')
    dict_by_salary = get_salary_city('Получение средней зароботной платы GameDev по городам...', df_group)
    dict_by_city = get_amount_city('Получение доли вакансий GameDev по городам...', df_group)


    print(Fore.LIGHTGREEN_EX + 'Генерация графиков...')
    generate_image(salary_by_year, vac_by_year, salary_by_prof, vacancy_by_prof, dict_by_salary, dict_by_city[1])




