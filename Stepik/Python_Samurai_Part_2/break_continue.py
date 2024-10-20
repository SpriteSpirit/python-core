# while True:
#     x = input()
#
#     if not x:
#         break
# print('Get out from loop')


"""
Нахождение первого четного числа в списке
"""
# lst = [1, 3, 4, 11, 6, 7, 1, 12, 21]
# is_even = False
# even_number = None
# start = 0
#
# while start < len(lst):
#     if lst[start] % 2 == 0:
#         is_even = lst[start]
#         break
#     start += 1
#
# print(is_even)

"""
Создать список из нечетных чисел
"""
# lst = [1, 3, 4, 11, 6, 7, 1, 12, 21]
# odd_number_list = []
# start = 0
#
# while start < len(lst):
#     if lst[start] % 2 == 0:
#         start += 1
#         continue
#     odd_number_list.append(lst[start])
#     start += 1
#
# print(odd_number_list)

"""
В списке должны остаться только слова состоящие из букв
"""
# only_word_list = []
#
# while (user_input := input()) != '0':
#     if not user_input.isalpha():
#         continue
#
#     only_word_list.append(user_input)
#
#
# print(only_word_list)

"""
else в цикле while
"""

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'char']
# i = 0
#
# while i < len(lst):
#     if not isinstance(lst[i], int):
#         print(f'Index {i} has not int type. It has "{lst[i]}"')
#         break
#     i += 1
# else:
#     print('All elements in list are int')
# print('The loop is over')

"""
Суммировать только до трехзначных чисел.
# """
# total_sum = 0
#
# while (number := input()) != 'stop':
#     if int(number) // 1000 >= 1:
#         break
#
#     total_sum += number
# else:
#     print('The loop is over')
#
# print(f'Total sum: {total_sum}')

"""
На вход подается целое положительное число не равное 1. Необходимо определить минимальный делитель этого числа больше 1. 
То есть, если мы разделим введенное число на минимальный делитель - остатка не будет. 
К примеру минимальный делитель числа 8 равен 2.
"""
# i = 2
# number = int(input('number: '))
#
# while i <= number:
#     if number % i == 0:
#         print(i)
#         break
#     i += 1

"""
Необходимо создать бесконечный цикл. Запуск начинается с запроса целого числа.
Введенное число выводится на экран строкой:
"Вы ввели число: ..."
Если вы ввели "13", то цикл прерывается и выводится сообщение:

"Вы всё таки ввели 13, а я думал мы друзья..."
Если вводится не число, то выводится сообщение:

"Вы ввели не число"
Цикл при этом не прерывается.
"""

# while True:
#     user_input = input('number: ')
#
#     if user_input == '13':
#         print('Вы всё таки ввели 13, а я думал мы друзья...')
#         break
#
#     if not user_input.isdigit():
#         print('Вы ввели не число')
#         continue
#
#     print(f'Вы ввели число: {user_input}')


"""
Необходимо запустить бесконечный цикл. 
На каждой итерации будет запрашиваться число, все положительные числа необходимо суммировать и 
вывести эту сумму после окончания цикла. Окончание цикла происходит при вводе "0". 
Реализовать подсчет при помощи оператора continue.
"""
# total_sum = 0
#
# while True:
#     user_int = int(input())
#
#     if user_int < 0:
#         continue
#     elif user_int == 0:
#         break
#
#     total_sum += user_int
#
# print(total_sum)

"""
На премьере новой части фильма "Человек-паук 7: гвоздь мне в кеды" остались только билеты на последний ряд. 
В последнем ряду 10 мест(список от 1го до 10ти). Вы выбираете места для 5ти человек. 
В цикле нужно ввести номер места, которое вы бронируете и заменить номер на "x". 
И цикл заканчивается когда вы купите 5ть мест, нужно учесть тот момент, что могут вводиться одинаковые и 
несуществующие номера мест. Вывести на экран итоговый список. Используйте в решении оператор continue.
"""
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# people_count = 5
# i = 0
#
# while i < people_count:
#     user_input = int(input())
#
#     if user_input in lst:
#         lst[user_input - 1] = 'x'
#         i += 1
#     else:
#         continue
#
# print(lst)

"""
Вводится список слов в одну строку через пробел. 
Необходимо вывести на экран "ДА" если все слова более 4ех символов, либо "НЕТ" если есть хотя бы одно слово, 
не соответствующее условию.
"""

# lst = []
# user_lst = input().split()
# i = 0
#
# while i < len(user_lst):
#     if len(user_lst[i]) > 4:
#         i += 1
#         continue
#     else:
#         print("НЕТ")
#         break
# else:
#     print("ДА")

"""
Вам нужно реализовать программу регистрации на сайте. В цикле сначала происходит запрос логина пользователя, 
он должен быть более 5-ти символов иначе программа нам сообщит:
Логин должен содержать не менее 5 символов
Запрос начнется заново. Если логин валидный, далее начнется запрос пароля, он должен быть не менее 8 символов 
и содержать символы "%" и "#". Если пароль не подошел, программа нам сообщает:

Пароль менее 8 символов, либо не содержит символы "%#"
Начинаем все заново с запроса логина. Если пароль корректный, то цикл завершается и выводится строка:

Регистрация завершена!
"""

user_login = ''
user_password = ''

while True:
    if len(user_login := input('login: ')) < 5:
        print('Логин должен содержать не менее 5 символов')
        continue
    if len(user_password := input('password: ')) < 8 or not ('%' in user_password and '#' in user_password):
        print('Пароль менее 8 символов, либо не содержит символы "%#"')
        continue
    else:
        break

print('Регистрация завершена!')