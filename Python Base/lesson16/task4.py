class MyOpen:

    def __init__(self, filename, mode):
        self.__filename = filename
        self.__mode = mode

    def __enter__(self):
        self.__file = open(self.__filename, self.__mode)
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()


with MyOpen('hello', 'w') as file:
    print(file.write('hello world'))

with MyOpen('hello', 'r') as file:
    print(file.read())
