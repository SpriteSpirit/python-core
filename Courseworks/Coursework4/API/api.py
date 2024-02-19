from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import fake_useragent


# Шаг 1: абстрактный класс для API
class JobAPI(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    @abstractmethod
    def parse_response(self, response):
        pass


'''
Создать абстрактный класс для работы с API сайтов с вакансиями. 
Реализовать классы, наследующиеся от абстрактного класса, для работы с 
конкретными платформами. 
Классы должны уметь подключаться к API и получать вакансии.
'''
