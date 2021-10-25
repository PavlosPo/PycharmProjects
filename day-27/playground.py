def add(*args):
    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num


# print(add(3, 4, 5, 6, 7))

def calculate(n, **kwargs):
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('color')



my_car = Car(make='Nissan')
print(my_car.model)
