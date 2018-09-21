class Person:
    __name = None
    __user_name = None
    __mail = None
    __user_id = None

    def __init__(self,name,user_name,mail):
        self.__name = name
        self.__user_name = user_name
        self.__mail = mail

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_all(self, name, user_name, mail):
        self.__name = name
        self.__user_name = user_name
        self.__mail = mail

    def get_all(self):
        return self.__name, self.__user_name, self.__mail
    def Format(self):
        return str(self.__name) + ' is my name'

person1 = Person('sebastian', 'sebbe', 'sebastian.edholm@gmail.com')

print(person1.get_name())

person1.set_name('Adam')

print(person1.get_name())

print(person1.get_all())


print(person1.Format())
