class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def formats(self):
        the_string = self.__name + ' is great'
        return the_string

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



p1 = Person('Sebastian')
print(p1.formats)
p1.name =  'John'
print(p1.formats)
