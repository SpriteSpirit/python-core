import json


class JSONSaver:
    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, "a") as file:
            json.dump(vacancy.__dict__, file)
            file.write("\n")

    def get_vacancies_by_salary(self, salary_range):
        # Этот метод требует дополнительной реализации
        pass

    def delete_vacancy(self, vacancy):
        # Этот метод требует дополнительной реализации
        pass
