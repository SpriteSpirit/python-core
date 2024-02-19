class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f'{self.title}, {self.link}, {self.salary}, {self.description}'
