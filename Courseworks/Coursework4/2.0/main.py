from hh_sj import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy

def filter_vacancies(vacancies, keywords):
    """
    Фильтрует список вакансий по наличию ключевых слов в описании.

    :param vacancies: Список объектов Vacancy, которые нужно отфильтровать.
    :param keywords: Список строк с ключевыми словами для фильтрации.
    :return: Список объектов Vacancy, описание которых содержит все ключевые слова.
    """
    filtered = []
    for vacancy in vacancies:
        # Проверяем, содержит ли описание вакансии все ключевые слова
        if all(keyword.lower() in vacancy.description.lower() for keyword in keywords):
            filtered.append(vacancy)
    return filtered

def user_interaction():
    hh_api = HeadHunterAPI()
    # superjob_api = SuperJobAPI()

    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    # superjob_vacancies = superjob_api.get_vacancies(search_query)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # Пример преобразования данных API в объекты Vacancy и фильтрация (для hh.ru)
    vacancies_objects = [
        Vacancy(
            v['name'],
            v['alternate_url'],
            v.get('salary', {}).get('from') if v.get('salary') is not None else None,
            v['snippet']['requirement']
        ) for v in hh_vacancies
    ]
    print(vacancies_objects)
    filtered_vacancies = filter_vacancies(vacancies_objects, filter_words)
    print(filtered_vacancies)
    # Вывод отфильтрованных вакансий пользователю
    if filtered_vacancies:
        print("\nНайденные вакансии:")
        for vacancy in filtered_vacancies:
            print(f"Название: {vacancy.name}")
            print(f"Ссылка: {vacancy.url}")
            print(f"Зарплата от: {vacancy.salary if vacancy.salary else 'не указана'}")
            print(f"Требования: {vacancy.description}\n")
    else:
        print("По вашему запросу вакансий не найдено.")


if __name__ == "__main__":
    user_interaction()
