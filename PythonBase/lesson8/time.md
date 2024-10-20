Интро: для чего нужны даты
Сложно представить систему, не использующую работу с датой. Приложения фиксируют время, когда что-то произошло (например, системы документооборота), делают расчеты, исходя из времени (например, спортивные приложения) и даже предсказывают время (например, системы заказа такси или доставки).

В этом эпизоде мы научимся получать дату и форматировать ее, а еще работать с текущей датой. Поехали!

Формат хранения даты
Дата и время реализуются с помощью специальных объектов. Определенная дата выбирается для начала отсчета (1 января 1970 года), а все остальные отсчитываются в секундах от этой даты. Число может быть и отрицательным. Например:

1 января 1970 года полдень — это 43200
1 января 2000 года полночь — это 946688400
31 января 1956 года (день рождения Гвидо) — это −439214400
Для большей точности дату можно хранить и в миллисекундах, тогда каждая дата будет больше в 1000 раз. Например, полдень 1 января 1970 года с миллисекундной точностью — это уже 43200000!

Попробуйте сервис Epoch Converter(https://www.epochconverter.com/) — переведите дату в число и обратно.

Начало работы с датой
Первое, что нужно сделать, — импортировать модуль с данными. По умолчанию он недоступен. В зависимости от задачи мы можем создать объекты нескольких типов:

дату (from datetime import date),
время (from datetime import time),
время и дату (from datetime import datetime).
Чтобы создать дату, укажите год, месяц и число:

date(<год>, <месяц>, <число>)

Обратите внимание, когда мы задаем время или дату, то всегда указываем цифры от большего к меньшему.

from datetime import date

date_one = date(1815, 12, 12) # 12 декабря 1815

print(date_one)

# Выведет 1815-12-12
 

Создаем время
При создании времени мы указываем часы, минуты и секунды:

time(<часы>, <минуты>, <секунды>)

from datetime import time

time_one = time(16, 20, 00) # 16 часов 20 минут

print(time_one)

# Выведет 16:20:00
 

Создаем время с датой
При создании времени вместе с датой мы указываем всё вместе, начиная с года и заканчивая секундами, а то, что мы не укажем, считается равным нулю:

datetime( <год>, <месяц>, <число>, <часы>, <минуты>, <секунды>)

from datetime import datetime

datetime_one = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47

print(datetime_one)

# Выведет 1986-04-26 01:23:47
 

Такие три основные типа данных существуют. Чаще всего используется 
datetime
, так как он хранит дату с точностью до секунды. Выбирайте тип, подходящий под свои задачи.

Работа с объектом даты
Чтобы работать с датой, есть специальные методы, например:

 

thedate.year
Вернет год
thedate.month
Вернет месяц
thedate.day
Вернет день
thedate.hour
Вернет час
thedate.minute
Вернет минуту
thedate.second
Вернет секунду
 

Посмотрим, как это работает на примере:

 

from datetime import datetime

thedate = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47

print("Год", thedate.year)
print("Месяц", thedate.month)
print("День", thedate.day)
print("Час", thedate.hour)
print("Минута", thedate.minute)
print("Секунда", thedate.second)

# Выведет

Год 1986
Месяц 4
День 26
Час 1
Минута 23
Секунда 47
 

Также есть функция weekday(), которая вернет день недели:

 

from datetime import date

thedate = date(1970, 1, 5)

print(thedate.weekday())

# Выведет  0, ведь понедельник — нулевой день недели!
 

Работа с текущей датой
Чтобы узнать, сколько сейчас времени и какой сейчас день, просто вызовите у datetime метод now и сразу получите нужный datetime. Обратите внимание, для date и time такого метода нет. А жаль.

from datetime import datetime

thedate = datetime.now()

print(thedate)
 

Получение даты из строки
Поскольку не все форматы файлов и данных поддерживают дату и дата часто передается просто в виде строки, часто вы будете получать дату из строк. Для этого есть метод fromisoformat(<строка даты>), который позволяет вытащить дату в 
date
, 
time
, 
datetime
.

Пример с датой:

 

from datetime import date

thedate = date.fromisoformat("2021-05-04")

print(thedate.year)
print(thedate.month)
print(thedate.day)

# Выведет:

2021
5
4
 

Пример со временем:

 

from datetime import time

thetime = time.fromisoformat("23:14")

print(thetime.hour)
print(thetime.minute)

# Выведет:

23
14
 

Пример с датой и временем:

 

from datetime import datetime

thedate = datetime.fromisoformat("2020-12-06 23:14")

print(thedate.year)
print(thedate.month)
print(thedate.day)

print(thedate.hour)
print(thedate.minute)

# Выведет:

2020
12
6
23
14
 

Форматирование даты
Если вам не нравится доставать время и дату по кусочкам, можно форматировать ее с помощью метода 
strftime()
 (от string format time) и специальной строки-шаблона, например:

from datetime import date

thedate = date(1970, 1, 5)

date_formatted = thedate.strftime("%d %B %Y ") # День Месяц Год

print(date_formatted)

# Выведет 05 January 1970
Вот какие буквы вы можете использовать:

%y
Год, короткая версия
18
%Y
Год, полная версия
2018
%m
Месяц номером
04
%B
Месяц словом
April
%d
День, от 01 до 31
12
%H
Час, от 00 до 23
04
%M
Минуты, от 00 до 59
23
%S
Секунды, от 00 до 59
07
И другие.

Вычисление разницы между датами
Часто в приложениях можно встретить уведомления типа «отправлено 2 часа назад», или «до вашего рейса осталось 15 минут», или «вот ваши фотографии год назад». Высчитывать промежуток между двумя датами можно с помощью timedelta. Например, можно узнать, сколько времени прошло между 7:10 и 7:30:

from datetime import date

# Задает первую дату
time_one = date(2020, 10, 1)
# Задает вторую дату
time_two = date(2020, 10, 2)

# Вычисляет расстояние в формате timedelta
delta = time_two - time_one

print(delta)

# Выведет 1 day, 0:00:00
Timedelta можно считать для типов date и datetime.

Дополнительные материалы
Работа с DateTime (видео): https://www.youtube.com/watch?v=bQhFZIwxSrw

Работа с датой и временем: https://pythonist.ru/rabota-s-datoj-i-vremenem-modul-datetime/