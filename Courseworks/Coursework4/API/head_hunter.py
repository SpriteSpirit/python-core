from abc import ABC
from Courseworks.Coursework4.API.api import JobAPI
import requests


class HeadHunterAPI(JobAPI, ABC):
    """

    """
    def get_vacancies(self, keyword: str):
        headers = {
            "Host": "https://api.hh.ru/",
            "User-Agent": "Safari",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        response = requests.get("API_ENDPOINT", headers=headers, params={"text": keyword, "area": "113"})
        response.raise_for_status()  # Проверка на ошибки запроса
        return response.json() # Возврат данных в формате JSON


