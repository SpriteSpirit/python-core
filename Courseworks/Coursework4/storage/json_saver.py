import os
import time
from data_saver import DataSaver
import json
import requests


# Шаг 3.1: Абстрактный класс и JSONSaver
class JSONSaver(DataSaver):
    """"""

    def __init__(self, filename: str):
        self.filename = filename

        if os.path.isfile(filename):
            print(f"Файл {filename} существует.")
        else:
            print(f"Файл {filename} не найден.")

    def add_vacancy(self, vacancy):
        """
        Добавление вакансии в файл
        :param vacancy:
        :return:
        """
        try:
            data = json.load(open(self.filename))
        except FileNotFoundError:
            data = []

        data.append(vacancy.__dict__)

        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def get_vacancies(self, criteria):
        """
        Получение вакансии из файла по критериям.
        :param criteria: Словарь с критериями поиска (например, {"title": "Python"})
        :return: Список вакансий, соответствующих критериям
        """
        # Справочник для параметров GET-запроса
        params = {
            'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 'Москва',  # Поиск осуществляется по вакансиям города Москва
            'only_with_salary': True,
            'salary': 100000,  # Поиск осуществляется по зарплате от
            'page': page,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params=params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        return data
        #
        # filtered_vacancies = []
        #
        # try:
        #     with open(self.filename, 'r', encoding='utf-8') as file:
        #         vacancies = json.load(file)
        #         match = False
        #
        #         for vacancy in vacancies:
        #             for k_vacancy, v_vacancy in vacancies.items():
        #                 # print(k_vacancy, v_vacancy)
        #                 for k_criteria, v_criteria in criteria.items():
        #                     if not isinstance(v_vacancy, dict):
        #                         if k_vacancy == 'name' and k_vacancy in k_criteria and v_criteria in v_vacancy:
        #                             # print(vacancies[k_vacancy])
        #                             match = True
        #                     else:
        #                         if k_vacancy == 'salary' and k_vacancy in k_criteria:
        #                             # print(vacancies[k_vacancy]['from'])
        #                             match = True
        #                         if k_vacancy == 'area' and k_vacancy in k_criteria:
        #                             # print(vacancies[k_vacancy]['name'])
        #                             match = True
        #                         if k_vacancy == 'experience' and k_vacancy in k_criteria:
        #                             # print(vacancies[k_vacancy]['name'])
        #                             match = True
        #         if match:
        #             filtered_vacancies.append(vacancy)
        # except FileNotFoundError:
        #     print("Файл с вакансиями не найден.")
        # except json.JSONDecodeError:
        #     print("Ошибка чтения файла с вакансиями.")
        #
        # return filtered_vacancies

    def delete_vacancies(self, vacancy):
        """
        Удаление вакансии из файла
        :param vacancy:
        :return:
        """
        try:
            data = json.load(open(self.filename))
            data.remove(vacancy.__dict__)

            with open(self.filename, 'w') as file:
                json.dump(data, file)
        except ValueError:
            print("Вакансия не найдена.")


def getArea(area_id: int = 113):
    req = requests.get('https://api.hh.ru/areas/countries')
    data = req.content.decode()
    req.close()
    all_countries = json.loads(data)

    for country in all_countries:
        if country['id'] == str(area_id):
            print(country)


# getArea()

#
# json_saver = JSONSaver('test.json')
#
# criteria = {
#     "name": input("Должность: "),
#     "salary": int(input("Зарплата от: ")),
#     "area": input("Город: "),
#     "experience_name": input("Опыт работы: ")
# }
# matching_vacancies = json_saver.get_vacancies(criteria)
# for vacancy in matching_vacancies:
#     print(vacancy)
#

# Функция для получения вакансий
def get_vacancies(city, vacancy, page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': f"{vacancy} {city}",
        'area': city,
        'specialization': 1,
        'per_page': 100,
        'page': page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def getPage(city, vacancy, page=0):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """

    # Справочник для параметров GET-запроса
    params = {
        'text': f'NAME:{vacancy}',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 1,  # Поиск осуществляется по вакансиям города Москва
        'only_with_salary' : True,
        'salary.from': 100000, # Поиск осуществляется по зарплате от
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }

    req = requests.get('https://api.hh.ru/vacancies', params=params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


# Считываем первые 2000 вакансий
for page in range(0, 5):

    # Преобразуем текст ответа запроса в справочник Python
    jsObj = json.loads(getPage('Москва', 'Аналитик', page))

    # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
    # Определяем количество файлов в папке для сохранения документа с ответом запроса
    # Полученное значение используем для формирования имени документа
    nextFileName = 'docs/pagination/{}.json'.format(len(os.listdir('docs/pagination')))

    # Создаем новый документ, записываем в него ответ запроса, после закрываем
    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    # Проверка на последнюю страницу, если вакансий меньше 2000
    if (jsObj['pages'] - page) <= 1:
        break

    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы можем подождать
    time.sleep(0.25)

print('Страницы поиска собраны')
#
# # Функция для получения отрасли компании
# def get_industry(company_id):
#     # Получение отрасли компании по ее идентификатору
#     if company_id is None:
#         return 'Unknown'
#
#     url = f'https://api.hh.ru/employers/{company_id}'
#     response = requests.get(url)
#     if response.status_code == 404:
#         return 'Unknown'
#     response.raise_for_status()
#     data = response.json()
#
#     if 'industries' in data and len(data['industries']) > 0:
#         return data['industries'][0].get('name')
#     return 'Unknown'
#
# # Функция для получения навыков вакансии
# def get_vacancy_skills(vacancy_id):
#     url = f'https://api.hh.ru/vacancies/{vacancy_id}'
#
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#
#     skills = [skill['name'] for skill in data.get('key_skills', [])]
#     return ', '.join(skills)
#
# # Функция для парсинга вакансий
# def parse_vacancies(psycopg2=None):
#     cities = {
#         'Москва': 1,
#         'Санкт-Петербург': 2
#     }
#
#     vacancies = [
#         'BI Developer', 'Business Development Manager', 'Community Manager', 'Computer vision',
#         'Data Analyst', 'Data Engineer', 'Data Science', 'Data Scientist', 'ML Engineer',
#         'Machine Learning Engineer', 'ML OPS инженер', 'ML-разработчик', 'Machine Learning',
#         'Product Manager', 'Python Developer', 'Web Analyst', 'Аналитик данных',
#         'Бизнес-аналитик', 'Веб-аналитик', 'Системный аналитик', 'Финансовый аналитик'
#     ]
#     for city, city_id in cities.items():
#         for vacancy in vacancies:
#             page = 0
#             while True:
#                 data = get_vacancies(city_id, vacancy, page)
#
#                 if not data.get('items'):
#                     break
#
#                 for item in data['items']:
#                     if vacancy.lower() not in item['name'].lower():
#                         continue  # Пропустить, если название вакансии не совпадает
#
#                     title = f"{item['name']} ({city})"
#                     keywords = item['snippet'].get('requirement', '')
#                     skills = get_vacancy_skills(item['id'])
#                     company = item['employer']['name']
#                     industry = get_industry(item['employer'].get('id'))
#                     experience = item['experience'].get('name', '')
#                     salary = item['salary']
#                     if salary is None:
#                         salary = "з/п не указана"
#                     else:
#                         salary = salary.get('from', '')
#                     url = item['alternate_url']
#
#                     insert_query = """
#                         INSERT INTO vacancies
#                         (city, company, industry, title, keywords, skills, experience, salary, url)
#                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     """
#                 if page >= data['pages'] - 1:
#                     break
#
#                 page += 1
#
#                 # Задержка между запросами в пределах 1-3 секунд
#                 time.sleep(random.uniform(3, 6))
#
#
#
# print(parse_vacancies())
