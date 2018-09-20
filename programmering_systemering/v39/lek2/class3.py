# Fördelen med properties är att du har ett sett hämta och sätta attribut oavsett om variablen
# är private eller public.
# Du kan köra kontrollers i ditt attribut för att kolla om värdet är ok.

class Person:
    """ This is my person class. Can I do this better?"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def formats(self):
        the_string = self.__name + ' is great'
        return the_string

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 120:
            self.__age = 80
            print("That's too old, age is set to 80")
        else:
            self.__age

    @name.setter
    def name(self, name):
        self.__name = name



p1 = Person('Sebastian', 32)
print(p1.formats)
p1.name =  'John'
print(p1.formats)
p1.age = 155
print(p1.age)
