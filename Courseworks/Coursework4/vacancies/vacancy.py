from abc import ABC, abstractmethod
import requests
import json


# Шаг 2: класс для работы с вакансиями
class Vacancy:
    """ Класс для работы с вакансиями"""
    def __init__(self, title: str, salary: str, description: str, link: str):
        self.title = title
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.link = link

    def __lt__(self, other: int):
        return self.salary < other.salary

    @staticmethod
    def cast_to_object_list(data: json):
        vacancies_list = []

        for item in data["items"]:
            vacancies_list.append(Vacancy(
                item['name'],
                item['alternate_url'],
                item.get('salary', {}).get('from'),
                item['snippet']['requirement']
            ))

        return vacancies_list

    def get_city(self):
        pass


    def get_salary(self):
        pass


    def get_name(self):
        pass
'''
Создать класс для работы с вакансиями. 
В этом классе самостоятельно определить атрибуты, такие как название вакансии, 
ссылка на вакансию, зарплата, краткое описание или требования и т. п. (не менее четырех). 
Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать 
данные, которыми инициализируются его атрибуты.
'''
