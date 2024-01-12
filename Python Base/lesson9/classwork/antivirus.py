virus_code = 'I am a virus'

with open("write_file.py") as file:
    content = file.read()

    if virus_code in content:
        print("Detected virus!")
    else:
        print("It is ok")
        