import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        self.y = 100
        del self.y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        self.y = 100
        del self.y


point = Point(1, 2)
point.z = 100
print(point.__dict__)

point_slots = PointSlots(3, 4)
# point_slots.z = 100
# print(point_slots.__dict__)

time1 = timeit.timeit(point.get_set_del)
time2 = timeit.timeit(point_slots.get_set_del)

print(f'time1: {time1:.2f}, time2: {time2:.2f}')