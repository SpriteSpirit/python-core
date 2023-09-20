# переменные счёта и награда за верные ответы
score = 0
award = 3
attempts = 3

# списки вопросов и верных ответов
questions = ["My name ___ Vova. ", "I ___ a coder. ", "I live ___ Moscow. ", "Where ___ you from? "]
answers = ["is", "am", "in", "are"]

# приветствие и приглашение
greeting = 'Привет! Предлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать!\n'
start = input(greeting)

if start == "ready":
    correct_answers = 0
    for i in range(len(questions)):
        while attempts > 0:
            user_answer = input(questions[i])
            if user_answer.lower() == answers[i]:
                score += award
                correct_answers += 1
                print(f"Ответ верный!\nВы получаете {award} баллов!\n")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    award -= 1
                    print(f"Ответ неверный! Осталось попыток: {attempts}.")
                else:
                    print("У вас закончились попытки.")

    total_percent = round(correct_answers * (100/len(questions)))

    end_congrats = f"Вот и всё! Вы ответили на {correct_answers} вопросов из {len(questions)} верно. Вы заработали {score} баллов. Это {total_percent} %."
    print(end_congrats)
else:
    print("Кажется, вы не хотите играть. Очень жаль.")
"""

# переменные счёта и награды за верные ответы
score = 0
award = 10

# списки вопросов и верных ответов
questions = ["My name ___ Vova. ", "I ___ a coder. ", "I live ___ Moscow. ", "Where ___ you from? "]
answers = ["is", "am", "in", "are"]

# приветствие и приглашение
greeting = 'Привет! Предлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать!\n'
start = input(greeting)

if start == "ready":
  for i in range(len(questions)):
      user_answer = input(questions[i])
      if user_answer.lower() == answers[i]:
          score += award
          print(f"Ответ верный!\nВы получаете {award} баллов!\n")
      else:
          print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")

  # результаты
  total_questions = score // award
  total_percent = round((total_questions * 100) / len(questions), 2)

  # поздравления и отчет
  end_congrats = f"Вот и всё! Вы ответили на {total_questions} вопросов из {len(questions)} верно. Вы заработали {score} баллов. Это {total_percent} %."
  print(end_congrats)
else:
  print("Кажется, вы не хотите играть. Очень жаль.")
"""