import sys
import time

from parse_hh_data import download, parse
import json
import requests

from functools import wraps
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, ConnectionError, Timeout
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# from .parse import num_pages as parse_num_pages
# from .parse import resume_hashes as parse_resume_hashes

SOFTWARE_NAMES = [SoftwareName.CHROME.value]
OPERATING_SYSTEMS = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
USER_AGENT = UserAgent(software_names=SOFTWARE_NAMES, operating_systems=OPERATING_SYSTEMS, limit=100)
VACANCY_URL = "https://api.hh.ru/vacancies/{}"
VACANCY_PAGE_URL = "https://api.hh.ru/vacancies?area={}&specialization={}&period={}&page={}&per_page=100"
AREAS_URL = "https://api.hh.ru/areas"

vacancy = download.vacancy_ids


def download(get_url):
    @wraps(get_url)
    def wrapper(*args, timeout=10, requests_interval=10, max_requests_number=100, break_reasons=None):
        """
        :param int requests_interval: time interval between requests (sec.)
        :param int max_requests_number: maximum number of requests
        :param list break_reasons: list of reasons
        """
        url = get_url(*args)
        break_reasons = set() if break_reasons is None else set(break_reasons)

        for _ in range(max_requests_number):
            try:
                request = requests.get(url, headers={'User-Agent': USER_AGENT.get_random_user_agent()}, timeout=timeout)
                request.raise_for_status()
            except ConnectionError as connection_error:
                print(f"Connection error occurred: {connection_error}", file=sys.stderr)
            except Timeout as time_out:
                print(f"Timeout error occurred: {time_out}", file=sys.stderr)
            except HTTPError as http_error:
                print(f"HTTP error occurred: {http_error}", file=sys.stderr)
                if request.reason in break_reasons:
                    break
            else:
                return request.content

            print(f"A second request to the {url} will be sent in {requests_interval} seconds")
            time.sleep(requests_interval)

        raise HTTPError(f"Page on this {url} has not been downloaded")
    return wrapper


def load_json(get_content):
    @wraps(get_content)
    def wrapper(*args, **kwargs):
        return json.loads(get_content(*args, **kwargs))
    return wrapper


def parse_html(get_content):
    @wraps(get_content)
    def wrapper(*args, **kwargs):
        return BeautifulSoup(get_content(*args, **kwargs), "html.parser")
    return wrapper


@load_json
@download
def areas():
    """
    :return: str
    """
    return AREAS_URL

@load_json
@download
def vacancy_search_page(area_name, specialization_id, search_period, num_page):
    """
    :param area_id: area identifier from https://api.hh.ru/areas
    :param specialization_id: specialization identifier from https://api.hh.ru/specializations
    :param int search_period: the number of days for search, max value 30
    :param num_page: page number
    :return: str
    """
    return VACANCY_PAGE_URL.format(area_name, specialization_id, search_period, num_page)


@load_json
@download
def vacancy(name):
    """
    :param str identifier: vacancy identifier
    :return: str
    """
    return VACANCY_URL.format(name)


def vacancy_ids(area_name, specialization_id, search_period, num_pages, **kwargs):
    """
    :param area_name: area identifier from https://api.hh.ru/areas
    :param specialization_id: specialization identifier from https://api.hh.ru/specializations
    :param search_period: the number of days for search
    :param num_pages: number pages for download
    :return: list
    """
    if num_pages is None:
        num_pages = 19

    ids = []
    for num_page in range(num_pages):
        page = vacancy_search_page(area_name, specialization_id, search_period, num_page, **kwargs)

        if not page["items"]:
            break

        ids.extend([item["name"] for item in page["items"]])

    return list(set(ids))


list_vac = vacancy_ids(113, 'Аналитик', 1, 3)
list = []

for id in list_vac:
    req = requests.get(f'https://api.hh.ru/vacancies/{id}')
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    # req.close()
    print(req.text)
    # list.append(data)

# print(list)