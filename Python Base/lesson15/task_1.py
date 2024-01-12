class Rectangle:
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def perimetr(self):
        return (self.__width + self.__height) * 2

    def area(self):
        return self.__width * self.__height

    def display(self):
        return f'Length: {self.__height}\nWidth: {self.__width}\nPerimetr: {self.perimetr()}\nArea: {self.area()}'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, unit: float):
        self.__width = unit

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, unit: float):
        self.__height = unit


if __name__ == '__main__':
    rect1 = Rectangle(15, 15)

    # TestCase#1: perimetr
    assert rect1.perimetr() == 60
    rect2 = Rectangle(10, 15)
    assert rect2.perimetr() == 50

    # TestCase#2: area
    assert rect1.area() == 225
    rect2 = Rectangle(10, 15)
    assert rect2.area() == 150

    # TestCase#3: display
    assert rect1.display() == 'Length: 15\nWidth: 15\nPerimetr: 60\nArea: 225'
    assert rect2.display() == 'Length: 15\nWidth: 10\nPerimetr: 50\nArea: 150'

    # TestCase#4: set width
    rect1.width = 20
    assert rect1.width == 20
    rect2.width = 50
    assert rect2.width == 50

    # TestCase#5: set height
    rect1.height = 10
    assert rect1.height == 10
    rect2.height = 5
    assert rect2.height == 5
