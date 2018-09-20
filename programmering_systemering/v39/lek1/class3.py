def hi(obj):
    print('Hi I am ' + obj.name + '!')

class Person:
    pass

x = Person()
x.name = 'Hello'
hi(x)
