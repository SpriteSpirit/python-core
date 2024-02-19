from abc import ABC, abstractmethod
import requests
import json


# Шаг 3.0: Абстрактный класс
class DataSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancies(self, vacancy):
        pass


'''
Определить абстрактный класс, который обязывает реализовать методы 
для добавления вакансий в файл, получения данных из файла по указанным 
критериям и удаления информации о вакансиях. Создать класс для 
сохранения информации о вакансиях в JSON-файл. Дополнительно 
(по желанию) можно реализовать классы для работы с другими форматами, 
например с CSV-, Excel- или TXT-файлом.
'''
