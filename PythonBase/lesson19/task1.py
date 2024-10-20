class TryExcept:

    def func1(self):
        self.func2()
        print('Regular func1 working')

    def func2(self):
        self.func3()
        print('Regular func2 working')

    def func3(self):
        try:
            100 / 0
        except ZeroDivisionError:
            print('ZeroDivisionError in func3')

        print('Regular func3 working')


some_obj = TryExcept()
some_obj.func1()
