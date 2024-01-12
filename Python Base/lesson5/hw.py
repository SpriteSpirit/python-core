import colorama

red = colorama.Fore.LIGHTRED_EX
white = colorama.Fore.LIGHTWHITE_EX
green = colorama.Fore.LIGHTGREEN_EX
yellow = colorama.Fore.LIGHTYELLOW_EX
cyan = colorama.Fore.LIGHTCYAN_EX
blue = colorama.Fore.LIGHTBLUE_EX

WORDS_EASY = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

WORDS_MEDIUM = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

WORDS_HARD = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

words_by_level = {"легкий": WORDS_EASY, "средний": WORDS_MEDIUM, "сложный": WORDS_HARD}

LEVELS = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}


# 1 step
def choose_level(words: dict) -> str:
    """
    Проверяем валидацию данных.
    Функция запрашивает у пользователя выбор уровня до тех пор,
    пока ввод не будет корректным
    :return: выбор пользователя = строковый ключ словаря words
    """

    choice = ""

    while choice.lower() not in words:
        program_answer(f"{white}Выберите уровень сложности.")
        program_answer(f"{green}легкий, {yellow}средний, {red}сложный.")

        choice = user_answer()

        if choice.lower() in words:
            for level in words:
                if choice.lower() == level:
                    program_answer(
                        f"{white}Выбран {blue}[{level.upper()}]{white} уровень"
                    )
                    program_answer(f"{white}Мы предложим 5 слов, подберите перевод.")

                    return level
        else:
            program_answer(f"{red}Такого режима нет. Попробуй снова.")


# 2 step
def questions(words, level: str) -> dict:
    """
    Функция собирает вопрос: слово для перевода,
    кол-во букв в переведенном и первую букву переведенного слова.
    Далее сравнивает ответ и вносит результаты в словарь с ответами.
    :param words: Словарь с уровнями сложности
    :param level: Выбранный юзером уровень сложности
    :return: Словарь с ответами (где ключ - слово англ., а знач. - верный/неверный ответ)
    """
    for en, ru in words[level].items():
        program_answer(
            f"{yellow}[{en}], {white}{len(ru)} букв(-ы), начинается на {yellow}[{ru[0]}...]"
        )

        user = user_answer()

        if user.lower() == ru:
            program_answer(f"{green}Верно, {yellow}[{en}]{white} — это {yellow}[{ru}].")
            answers[en] = True
        else:
            program_answer(f"{red}Неверно. {yellow}[{en}]{white} — это {yellow}[{ru}].")
            answers[en] = False

    return answers


# 3 step
def results(total_answers: dict) -> None:
    """
    Функция сортирует ключи-значения по спискам верных/неверных ответов юзера.
    Далее выводит результаты.
    :param total_answers: Словарь с ответами (где ключ - слово англ., а знач. - верный/неверный ответ)
    :return: None
    """
    true_list = []
    false_list = []

    for answer, result in total_answers.items():
        if result:
            true_list.append(answer)
        else:
            false_list.append(answer)

    text_decorator(f"{yellow}результаты")

    if len(true_list) != 0:
        print(f"{green}Правильно переведенные слова:{white}")
        print("\n".join([answer for answer in true_list]))
    else:
        print(f"{red}Увы, верно переведенных слов нет!")

    separator()

    if len(false_list) != 0:
        print(f"{red}Неправильно переведенные слова:{white}")
        print("\n".join([answer for answer in false_list]))
    else:
        print(f"{green}Поздравляем! Неверно переведенных слов нет!")

    separator()
    program_answer(
        f"{white}Поздравляем! Ваш уровень - {yellow}[{LEVELS[len(true_list)]}]{white}!"
    )


def separator() -> None:
    """
    Декоративный разделитель для визуального оформления
    :return:
    """
    print(f"{red}_ _" * 15)


def user_answer() -> str:
    """
    Фун-я принимает ответ пользователя вместе с разделителями
    :return: Ответ пользователя в виде строки
    """
    separator()
    user = input(f"{green}Пользователь: ")
    separator()

    return user


def program_answer(text: str) -> None:
    """
    Фун-я принимает текст для программы
    локально в местах использования.
    :param text: Принимает строку с текстом
    :return: None
    """
    print(f"{cyan}Программа: {text}")


def text_decorator(text: str) -> None:
    """
    Фун-я работает с декорацией текста по типу заголовка.
    :param text: Принимает строку с текстом
    :return: None
    """
    separator()
    print(" " * 15 + f"{yellow}{text.upper()}")
    separator()


# 4 step
def play() -> None:
    """
    Фун-я запускает игру один раз, используя функции:
    :func:choose_level: выбор уровня
    :func:questions:
    :func:results:
    """
    text_decorator("translate training 2.0")

    level = choose_level(words_by_level)
    summary = questions(words_by_level, level)
    results(summary)


# 5 step
play()
