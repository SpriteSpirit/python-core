'''# счет пользователя
score = 0
# награда за верные ответы
award = 10
# знакомство
greeting = 'Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут.\n'
# получаем имя пользователя
name = input(greeting)

print(f"Привет, {name}!\nLet's begin!\n")

# Вопрос 1
user_answer1 = input("My name ___ Vova. ")
true_answer1 = "is"

if user_answer1 == true_answer1:
    score += award
    print(f"Ответ верный!\nВы получаете {award} баллов!\n")
else:
    print(f"Неправильно.\nПравильный ответ: {true_answer1}\n")

# Вопрос 2
user_answer2 = input("I ___ a coder. ")
true_answer2 = "am"

if user_answer2 == true_answer2:
    score += award
    print(f"Ответ верный!\nВы получаете {award} баллов!\n")
else:
    print(f"Неправильно.\nПравильный ответ: {true_answer2}\n")

# Вопрос 3
user_answer3 = input("I live ___ Moscow. ")
true_answer3 = "in"

if user_answer3 == true_answer3:
    score += award
    print(f"Ответ верный!\nВы получаете {award} баллов!\n")
else:
    print(f"Неправильно.\nПравильный ответ: {true_answer3}\n")

# результаты
total_questions = score // award
total_percent = round(((score / 30) * 100), 2)

# поздравления-отчет
end_congrats = f"""Вот и всё, {name}!
Вы ответили на {total_questions} вопросов из 3 верно.
Вы заработали {score} баллов.
Это {total_percent} %."""

print(end_congrats)'''

# переменные счёта и награды за верные ответы
score = 0
award = 10

# приветствие и знакомство с пользователем
greeting = 'Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут.\n'
name = input(greeting)
print(f"Привет, {name}!\nLet's begin!\n")

# списки вопросов и верных ответов
questions = ["My name ___ Vova. ", "I ___ a coder. ", "I live ___ Moscow. "]
answers = ["is", "am", "in"]

# проходимся по индексам вопросов-ответов (при условии, что длина списков обоюдно равна)
# цикл выполнится от первого (0) до последнего элемента списка
for i in range(len(questions)):
    user_answer = input(questions[i])
    # если ответ пользователя равен верному ответу, то наргаждаем, если нет, то, выводим верный ответ
    if user_answer == answers[i]:
        score += award
        print(f"Ответ верный!\nВы получаете {award} баллов!\n")
    else:
        print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")

# результаты
total_questions = score // award
total_percent = round(((score / 30) * 100), 2)

# поздравления и отчет
end_congrats = f"""Вот и всё, {name}!
Вы ответили на {total_questions} вопросов из 3 верно.
Вы заработали {score} баллов.
Это {total_percent} %."""

print(end_congrats)