class ShebangShellException(Exception):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Должен быть шебанг'


class EmptyShellException(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Файл не должен быть пустым'


class ShellExecutor:

    def __init__(self, file_content):
        self.content = file_content

        if len(self.content) == 0:
            raise Exception

        if self.content[0] != '#':
            raise ShebangShellException('Need shebang')


# content ='#!/bin/bash' # правильно
content ='!/bin/bash' # не хватает шебанг
# (Шебанг (shebang) — строка комментария, начинающаяся с символов #!, которая играет важную роль в запуске скриптов на языках программирования Bash и Python.
# Шебанг указывает операционной системе, какой интерпретатор нужно использовать для выполнения скрипта.)
# content ='' # пустой скрипт

try:
    shell_executor = ShellExecutor(content)
except EmptyShellException as ex:
    print(ex.message)
except ShebangShellException as ex:
    print(ex.message)

