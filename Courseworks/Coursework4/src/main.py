# Шаг 5: Функция взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()


'''
Создать функцию для взаимодействия с пользователем. 
Функция должна взаимодействовать с пользователем через консоль. 
Самостоятельно придумать сценарии и возможности взаимодействия с 
пользователем. Например, позволять пользователю указывать, 
с каких платформ он хочет получить вакансии, ввести поисковый запрос, 
получить топ-N вакансий по зарплате, получить вакансии в 
отсортированном виде, получить вакансии, в описании которых есть 
определенные ключевые слова, например postgres, и т. п.
'''