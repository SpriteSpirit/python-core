'''import random

# Словарь с азбукой Морзе
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Список слов для расшифровки
words = ['code', 'bit', 'list', 'soul', 'next']

def morse_encode(word):
    """
    Функция преобразует слово на английском языке в последовательность точек и тире с помощью азбуки Морзе.

    Args:
        word (str): Слово на английском языке.

    Returns:
        str: Последовательность точек и тире, соответствующая слову в азбуке Морзе.
    """
    morse_word = ""
    for char in word:
        if char.upper() in morse_code:
            morse_word += morse_code[char.upper()] + " "
    return morse_word.strip()

def get_word():
    """
    Функция возвращает случайное слово из списка words.

    Returns:
        str: Случайное слово из списка words.
    """
    return random.choice(words)

def print_statistics(answers):
    """
    Функция выводит статистику ответов на задачи.

    Args:
        answers (list): Список ответов на задачи, где True - верный ответ, False - неверный ответ.
    """
    total = len(answers)
    correct = answers.count(True)
    incorrect = answers.count(False)
    print("Всего задачек:", total)
    print("Отвечено верно:", correct)
    print("Отвечено неверно:", incorrect)

def main():
    print("Сегодня мы потренируемся расшифровывать азбуку Морзе.")
    input("Нажмите Enter и начнем")

    answers = []

    for i in range(5):
        word = get_word()
        morse_word = morse_encode(word)

        print("Слово", i+1, "-", morse_word)
        user_word = input().strip()

        if user_word.lower() == word.lower():
            print("Верно,", word + "!")
            answers.append(True)
        else:
            print("Неверно,", word + "!")
            answers.append(False)

    print_statistics(answers)

if __name__ == "__main__":
    main()'''

for i in range(5):
    print(i + i * 1)