import json
import os
import time

import requests


def get_city(crit_city: str):
    areas = requests.get('https://api.hh.ru/areas').json()

    cities = {}

    for country in areas:
        if country['id'] == '113':
            for city in country['areas']:
                if 'areas' in city:
                    for subregion in city['areas']:
                        cities[subregion['name']] = city['id']
                cities[city['name']] = city['id']

    for city in cities.keys():
        if crit_city.lower() in city.lower():
            return cities[crit_city.title()]
        

def check_salary(vacancy, salary_from):
    filtered_vacancies = []
    for item in vacancy["items"]:
        salary = item['salary']
        if salary and salary['from'] is not None:
            if salary['from'] >= salary_from:
                filtered_vacancies.append(item)
    return filtered_vacancies


def getPage(city, vacancy, page=2):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """
    # Справочник для параметров GET-запроса
    params = {
        'text': f'NAME:{vacancy}',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': city,  # Поиск осуществляется по вакансиям города
        'only_with_salary' : True,
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }

    req = requests.get('https://api.hh.ru/vacancies', params=params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


def sorting(city, title_post, salary_from):

    # Считываем первые 2000 вакансий
    # for page in range(0, 5):

        # Преобразуем текст ответа запроса в справочник Python
    jsObj = json.loads(getPage(city, title_post))
    print(type(jsObj))
    print(jsObj)
        # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
        # Определяем количество файлов в папке для сохранения документа с ответом запроса
        # Полученное значение используем для формирования имени документа
    nextFileName = 'docs/pagination/{}.json'.format(len(os.listdir('docs/pagination')))

    result = sort_by_salary(jsObj, salary_from)
    # Создаем новый документ, записываем в него ответ запроса, после закрываем
    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(result, ensure_ascii=False))
    f.close()

    # Проверка на последнюю страницу, если вакансий меньше 2000
    # if (jsObj['pages'] - page) <= 1:
    #     break

    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
    # time.sleep(0.25)

    print('Страницы поиска собраны')

def sort_by_salary(object, salary_from):
    new_data = []  # создаем пустой список

    filtered_vacancies = check_salary(object, salary_from)
    if filtered_vacancies:
        new_data.append({"items": filtered_vacancies})

    return new_data  # возвращаем список


city = get_city(input('Выберите город: '))
title_post = input('Укажите должность: ')
salary_from = int(input('Укажите зарплату: '))
# print(sort_by_salary(350000))
# print(sort_by_salary(50_000))

sorting(city, title_post, salary_from)