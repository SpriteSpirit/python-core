def get_grade(grade: int) -> str:
    grade_list = ["Плохо", "Удовлетворительно", "Хорошо", "Отлично"]
    res = [grade_list[i] for i in range(len(grade_list)) if grade == i + 2]
    print(res)
    return res[0] if res else "Ошибка"


print(get_grade(int(input("grade: "))))

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")