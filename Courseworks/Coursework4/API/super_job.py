from abc import ABC
from Courseworks.Coursework4.API.api import JobAPI
import requests


class SuperJobAPI(JobAPI, ABC):
    """

    """

    def __init__(self, token):
        self.token = token

    def get_vacancies(self, keyword: str):
        headers = {"X-Api-App-Id": self.token}

        response = requests.get("API_ENDPOINT", headers=headers, params={"keyword": keyword})
        response.raise_for_status() # Проверка на ошибки запроса
        return response.json() # Возврат данных в формате JSON