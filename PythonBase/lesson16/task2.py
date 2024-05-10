class CustomStrip:

    def __init__(self, characters):
        self.__characters = characters

    def __call__(self, stc):
        return stc.strip(self.__characters)


cs = CustomStrip('!@#$')
string_to_clear = '@hello, world!#'

result = cs(string_to_clear)
print(result)