import numpy as np
import pandas as pd
import regex as re
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

    print(get_amount('Получение динамики вакансий по годам...', df_group))

    print(get_salary('Получение средней зароботлной платы за год...', df_group))

    print(Fore.LIGHTGREEN_EX + 'Поиск вакансий с критериями...')
    df = df[df['name'].str.contains('game|gamedev|unity|unreal|\bигр', regex=True, flags=re.IGNORECASE)] #Поиск всех вакансий с игровыми названиями
    df_group = df.groupby('year')

    print(get_amount('Получение динамики вакансий GameDev по годам...', df_group))

    print(get_salary('Получение средней зароботлной платы за год по вакансии GameDev...', df_group))



