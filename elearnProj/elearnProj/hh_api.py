import requests
import json
import time
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", "{:.2f}".format)

def get_page(page = 0):
    params = {
        'text': 'NAME:GameDev',
        'date_from': '2023-01-23T00:00:00+0300',
        'date_to': '2023-01-23T23:59:59+0300',
        'area': 1,
        'page': page,
        'per_page': 10
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data

def get_salary(x):
    try:
        res_from = dict(x).get('from', 'NaN')
        res_to = dict(x).get('to', 'NaN')
    except:
        return 'NaN'
    return str(res_from)+'-'+str(res_to)


def main_():
    js_objs = []
    obj_set = []

    for page in range(0, 1):
        js_obj = json.loads(get_page(page))
        js_objs.extend(js_obj['items'])
        if (js_obj['pages'] - page) <= 1:
            break
        time.sleep(0.25)

    res = []
    df = pd.DataFrame(js_objs)
    df['salary'] = df['salary'].apply(lambda x: 'Зарплата: ' + get_salary(x))
    df = df[['name', 'employer', 'salary', 'area', 'published_at']]
    df['employer'] = df['employer'].apply(lambda x: 'Заказчик: ' + dict(x)['name'])
    df['area'] = df['area'].apply(lambda x: 'Город: ' + dict(x)['name'])
    df['published_at'] = df['published_at'].apply(lambda x: 'Опубликовано в ' + x)

    result = [list(x) for x in df.values]
    return result

#print(main_())


'''
import requests
import json
import time
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", "{:.2f}".format)

def get_page(page = 0):
    params = {
        'text': 'NAME:GameDev',
        'date_from': '2022-22-22T00:00:00+0300',
        'date_to': '2022-22-22T23:59:59+0300',
        'area': 1,
        'page': page,
        'per_page': 10
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data

def get_salary(x):
    try:
        res_from = dict(x).get('from', 'NaN')
        res_to = dict(x).get('to', 'NaN')
    except:
        return 'NaN'
    return str(res_from)+'-'+str(res_to)


def main():
    js_objs = []
    obj_set = []

    for page in range(0, 1):
        js_obj = json.loads(get_page(page))
        js_objs.extend(js_obj['items'])
        if (js_obj['pages'] - page) <= 1:
            break
        time.sleep(0.25)

    res = []
    df = pd.DataFrame(js_objs)
    df['salary'] = df['salary'].apply(lambda x: get_salary(x))
    df = df[['name', 'employer', 'salary', 'area', 'published_at']]
    df['employer'] = df['employer'].apply(lambda x: dict(x)['name'])
    df['area'] = df['area'].apply(lambda x: dict(x)['name'])

    return df

if __name__ == '__main__':
    print(main())'''