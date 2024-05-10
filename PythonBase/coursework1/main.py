import random

# список загаданных слов и пустой список ответов
encoding_word = ["code", "bit", "data_list", "soul", "next", "ice cream", "2023", "skypro"]
answers = []

# азбука Морзе (константа - словарь)
MORSE = {".": ".-.-.-", ",": "--..--", "?": "..--..",
         "!": "-.-.--", "-": "-....-", "/": "-..-.",
         "@": ".--.-.", "(": "-.--.",  ")": "-.--.-",

         "0": "-----", "1": ".----",
         "2": "..---", "3": "...--",
         "4": "....-", "5": ".....",
         "6": "-....", "7": "--...",
         "8": "---..", "9": "----.",

         "a": ".-",   "b": "-...",
         "c": "-.-.", "d": "-..",
         "e": ".",    "f": "..-.",
         "g": "--.",  "h": "....",
         "i": "..",   "j": ".---",
         "k": "-.-",  "l": ".-..",
         "m": "--",   "n": "-.",
         "o": "---",  "p": ".--.",
         "q": "--.-", "r": ".-.",
         "s": "...",  "t": "-",
         "u": "..-",  "v": "...-",
         "w": ".--",  "x": "-..-",
         "y": "-.--", "z": "--.."}


def morse_encode(word: str, morse_code: str) -> str:
    """
    Зашифровывает слово из азбуки Морзе
    независимо от регистра самой азбуки
    и собирает в переменной result результат в нижнем регистре

    :param word: передаем рандомное слово из списка
    :param morse_code: передаем саму азбуку Морзе
    :return: возвращает копию строки с удаленными пробелами [начало и конец строки]
    """

    result = ""
    for char in word:
        if char.lower() in morse_code:
            result += morse_code[char.lower()] + " "
        elif char.upper() in morse_code:
            result += morse_code[char.lower()] + " "

    return result.strip()


def get_word(words: list) -> str:
    """
      Получает случайное слово
      из списка слов
    """

    return random.choice(words)


def print_statistics(total_questions: int, all_answers: list) -> str:
    """
    Выводит статистику по [всего ответов],
    [верные ответы] и [не верные ответы]

    :param total_questions: передаем кол-во раз запуска игры в int значении
    :param all_answers: передаем список ответов пользователя
    :return: f-строку
    """

    return (f"\n"
            f"Всего задачек: {total_questions}\n"
            f"Отвечено верно: {all_answers.count(True)}\n"
            f"Отвечено неверно: {all_answers.count(False)}\n\n"
            f"Спасибо за игру!\n(〃￣︶￣)人(￣︶￣〃)")


def play():
    """
    Функция отвечает за игровой цикл и
    управляет количеством запуска цикла
    через параметр times (раз).

    If конструкция проверяет на равенство
    ответ пользователя с заданно-верным ответом программы.
    И пополняет список ответов булевыми значениями.

    Дополнительно чистим строковые ответы от пробелов.

    Игра запустится хотя бы один раз, если не будет указано кол-во.
    Если пользователь снова откажется, то прощаемся.
    """

    print("Сегодня мы потренируемся расшифровывать морзянку.")
    input("Нажмите Enter и начнем...")

    times = input("Сколько раз вы хотите сыграть?\n")

    if times is None or times == "0" or times == "":
        times = 1
        print(f"Мы всё равно сыграем {times} раз 👾")
        user_reaction = input("Договорились? ")

        if user_reaction.replace(" ", "").lower() == "нет" or \
                user_reaction.replace(" ","").lower() == "no" or \
                user_reaction.replace(" ", "") == "":
            print("Жаль! Ждём вас снова. 🥺")
            return

    print("Отлично! Поехали! 🤓\n")

    times = int(times)

    for i in range(times):
        word = get_word(encoding_word)
        morse_code = morse_encode(word, MORSE)
        # print(f"hint: {word}")
        # print(f"hint: {morse_code}")

        if i == 0:
            print("Программа:")

        print(f"Слово {i + 1} : {morse_code}\n")

        print("Пользователь:")
        user_word = input().strip()

        if user_word.replace(" ", "").lower() == word.replace(" ", "").lower():
            print(f"\nПрограмма:\nВерно, {word}!")
            answers.append(True)
        else:
            print(f"\nПрограмма:\nНе верно, {word}!")
            answers.append(False)

    # по окончании игры выводим статистику
    print(print_statistics(times, answers))


# запускаем игру
play()