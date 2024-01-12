virus_code = "print('I am a virus')"
with open("write_file.py", 'a') as file:  # append - дописывает информацию в конец строки
    print(file.write(f"\n{virus_code}\n"))
print(virus_code)