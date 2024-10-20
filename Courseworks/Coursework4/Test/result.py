import requests


def fetch_and_process_data(url):
    data = requests.get(url).json()
    return process_data(data)

processed_data = fetch_and_process_data('https://api.example.com/data')
processed_data2 = fetch_and_process_data('https://api.example.com/data2')
