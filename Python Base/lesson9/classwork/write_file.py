user_lang = input("What language are you learning: ")
user_time = input("How long ago: ")
user_institution= input("Where: ")

with open("answers.txt", "w", encoding="utf-8") as file:  # write, text
    file.write(f"{user_lang}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_institution}\n")

print('I am a virus')
