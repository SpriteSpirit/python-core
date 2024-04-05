"""# По умолчанию в земных сутках 24 часа, но, например, на Меркурии сутки длятся 1392 часа, а на Сатурне 10 часов. #
Напишите функцию, которая переводит часы в количество полных суток и возвращает полученное значение. Функция может
принимать вторым аргументом длительность суточного цикла, а может и не принимать. # # Пример работы функции: # print(
hours_to_days(48)) # Вернет 2 # print(hours_to_days(12)) # Вернет 0 # print(hours_to_days(36, 12))  # Вернет 3


def hours_to_days(hours: int, duration: int = 24) -> int:
    return hours // duration


values = [int(x) for x in input().split(" ")]
print(hours_to_days(*values))


# Функция get_distance(fuel, consumption) вычисляет, сколько пролетит самолет в зависимости от объема топлива на борту
# в литрах и расхода топлива на километр, и возвращает количество километров.
#
# По умолчанию каждый километр расходуется 20 литров, но мы можем переопределить это значение
# (например, если самолет перегружен, на каждый километр расходуется 25 литров).
#
# Пример ввода:
# get_distance(100) # Вернет 5.0
# get_distance(200) # Вернет 10.0
# get_distance(100, 20) # Вернет 5.0
# get_distance(100, 50) # Вернет 2.0
# get_distance(200, 50) # Вернет 4.0


def get_distance(fuel: float, consumption: float = 20) -> float:
    return fuel / consumption


values = [int(x) for x in input().split(" ")]
print(get_distance(*values))


# Напишите функцию count_successful(students, score), которая считает, сколько студентов прошли тестирование.
#
# Функция получает список оценок студентов (students) и возвращает количество студентов, которые набрали
# проходной балл (score). По умолчанию проходной балл равен 50, но мы можем передать и другое значение score.
#
# Пример ввода:
# count_successful([]) # Возвращает 0
# count_successful([50, 50]) # Возвращает 2
# count_successful([20, 20]) # Возвращает 0
# count_successful([40, 40], 40) # Возвращает 2
# count_successful([80, 40]) # Возвращает 1
# count_successful([80, 40], 40) # Возвращает 2
# count_successful([60, 60], 90) # Возвращает 0


def count_successful(students: data_list, score: int = 50) -> int:
    return len([point for point in students if point >= score])


values = [int(x) for x in input().split(" ")]
score_ = input()

print(
    count_successful(values, int(score_))
    if score_.isdigit()
    else count_successful(values)
)


# Напишите функцию, которая получает несколько элементов через пробел и суммирует их.
#
# Пример вызова функции:
# lost_time(1, 2, 3) # Вернет 6
# lost_time(3, 3, 3, 3) # Вернет 12


def lost_time(*nums: int) -> int:
    return sum([num for num in nums])


numbers = [int(x) for x in input().split(" ")]
print(lost_time(*numbers))
"""


def get_cd(dna: str) -> float:
    count = dna.count("C") + dna.count("G")
    return (count / len(dna)) * 100


print(get_cd("ATCGATCG"))
