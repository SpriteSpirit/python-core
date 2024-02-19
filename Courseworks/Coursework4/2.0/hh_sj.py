from api import JobSiteAPI
import requests


class HeadHunterAPI(JobSiteAPI):
    base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query):
        response = requests.get(self.base_url, params={"text": query})
        return response.json()['items']


class SuperJobAPI(JobSiteAPI):
    base_url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {"X-Api-App-Id": "your_app_id_here"}

    def get_vacancies(self, query):
        response = requests.get(self.base_url, headers=self.headers, params={"keyword": query})
        return response.json()['objects']
