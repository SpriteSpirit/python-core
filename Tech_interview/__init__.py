for index, letter in enumerate(['a', 'b', 'c']):
    print(index, letter)

for digit in [1, 2, 3]:
    print(digit)
    if digit == 2:
        print('срабатывает break')
        print('ELSE не выведется, если сработал break')
        break
else:
    print('ELSE отработал после всех итераций цикла без прерывания')
