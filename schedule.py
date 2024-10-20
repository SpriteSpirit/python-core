weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Суббота', 'Воскресенье']
        #   0        1        2        3        4        5        6        7        8        9        10       11
times = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
        # -12      -11      -10       -9       -8       -7       -6        -5      -4       -3       -2       -1
max_len = 0

for weekday in weekdays:
    if len(weekday) > max_len:
        max_len = len(weekday)

monday = f'{weekdays[0]} :: {times[0]} :: {times[3]} :: {times[4]}'
tuesday = f'{weekdays[1]}{" " * (max_len - len(weekdays[1]))} :: {times[2]} :: {times[4]}'
wednesday = f'{weekdays[2]}{" " * (max_len - len(weekdays[2]))} :: {times[0]} :: {times[2]} :: {times[3]} :: {times[-2]}'
thursday = f'{weekdays[3]}{" " * (max_len - len(weekdays[3]))} :: {times[2]} :: {times[3]}'

saturday = (f'{weekdays[4]}{" " * (max_len - len(weekdays[4]))} :: {times[2]}'
            f':: {times[4]} :: {times[5]}:: {times[-4]} :: {times[-2]}')
sunday = f'{weekdays[5]} :: Свободного времени нет'


print("_______________________________")
print("Время указано московское [GMT+3]")
print("_______________________________")
# print(monday)  # Понедельник
# print(tuesday)  # Вторник
print(wednesday)  # Среда
print(thursday)  # Четверг

# print(saturday)  # Суббота
# print(sunday)  # Воскресенье

