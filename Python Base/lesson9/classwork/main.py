'''
Открытие файлов
file = open('text.txt', 'rt')  # read, text
file = open('test.txt', 'rb')  # read, binary

text = file.read()  # в количестве параметра можем указать количество байт для считывания. Например, file.read(10)
print(text)

for line in file:
    print(line)

file.close()

book_count = 0

# такая конструкция позволяет сократить работу и не исп. закрытие файла
with open('books.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line)
        book_count += 1

print(f'Books: {book_count}')
'''

with open('books.txt', 'rt', encoding='utf-8') as file:
    book_count = len(file.readlines())


print(f'Books: {book_count}')
