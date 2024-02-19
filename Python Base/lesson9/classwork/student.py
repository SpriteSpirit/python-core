# по умолчанию чтение текстовых файлов

with open("students.txt") as file:
    for student_data in file:
        # data = student_data.rstrip("\n").split(": ")
        # name = data[0]
        # lang = data[1]
        # print(student_data)
        # print(student_data.rstrip("\n"))
        # print(student_data.rstrip("\n").split(": "))

        name, lang = student_data.rstrip("\n").split(": ")

        print(f"Студент {name} учит язык {lang}.")
