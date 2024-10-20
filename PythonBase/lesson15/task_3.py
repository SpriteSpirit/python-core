class DataBase:
    instance = None

    def __init__(self, user: str, psw: str, port: int):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data: str):
        print(f'Запись в БД {data}')

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == '__main__':
    db = DataBase('root', '1234', 80)
    db2 = DataBase('root2', '5678', 40)
    print(db is db2)  # Выведет: True


"""
Реализуйте магический метод 
__new__
 класса 
DataBase
 таким образом, что экземпляр этого класса должен присутствовать гарантированно в одном экземпляре при работе программы. То есть одновременно два объекта класса 
DataBase
 быть не должно. При попытке создать второй экземпляр просто возвращаем ссылку на ранее созданный экземпляр.

Ожидаемый вывод:

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(db is db2)
True
"""