# JAVA WAY
class JavaPerson:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) <= 0:
            self.__name = 'Anonymous'
        elif len(name) > 8:
            self.__name = 'Too long dude'
        else:
            self.__name = name

p1 = JavaPerson('Adam')
print(p1.get_name())


# Python way

class PyPerson:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


p2 = PyPerson('Sebastian')
print(p2.name)
p2.name = 'Dåre'
print(p2.name)
