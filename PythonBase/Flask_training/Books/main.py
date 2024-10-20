# Импортируем класс Flask и функцию render_template из модуля flask.
from flask import Flask, render_template

# Создаем экземпляр класса Flask и присваиваем его переменной app. __name__ - это имя текущего модуля.
app = Flask(__name__)


def get_films():
    """Определяем функцию get_films(), которая возвращает список словарей с информацией о фильмах."""
    return [
        {
            'id': 1,
            'title': 'Harry Potter and Philosopher\'s Stone',
            'release_date': 'November 4, 2001'
        },
        {
            'id': 2,
            'title': 'Harry Potter and Chamber of Secrets',
            'release_date': 'November 3, 2002'
        },
    ]


@app.route("/")
@app.route("/index")
def index():
    """Создаем маршруты с помощью декоратора @app.route(). Когда пользователь открывает главную страницу ("/") или
    страницу "/hello", вызывается функция index(). Функция получает список фильмов с помощью функции get_films() и
    отрисовывает шаблон "index.html", передавая в него список фильмов."""
    films = get_films()
    return render_template("index.html", films=films)


@app.route("/about")
def about():
    """Создаем маршрут "/about". Когда пользователь открывает страницу "/about", вызывается функция about(). Функция
    отрисовывает шаблон "about.html" и передает ему переменную title со значением "About"."""
    return render_template("about.html", title="About")


@app.route("/<string:name>")
def greeting(name):
    """Создаем маршрут с динамическим значением в url. Когда пользователь открывает страницу, в url передается имя
    пользователя. Функция greeting() принимает это имя в качестве аргумента, преобразует его в заглавные буквы и
    отрисовывает приветствие с этим именем."""
    return f"<h1>Hello, {name.capitalize()}!</h1>"


# app.create_jinja_environment()

# Проверяем, является ли текущий модуль главным (то есть запускается напрямую, а не импортируется).
# Если это так, запускаем сервер Flask с помощью метода run() объекта app.
if __name__ == "__main__":
    app.run()
