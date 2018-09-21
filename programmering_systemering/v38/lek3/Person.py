class Person:
    __name = None
    __user_name = None
    __mail = None
    __user_id = None
    __user_age = None

    def __init__(self, name, user_name, mail, age):
        self.__name = name
        self.__user_name = user_name
        self.__mail = mail
        self.__user_age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    #def set_all(self):
        #self.__name = input('Vad är ditt namn?> ')
        #self.__user_name = input('Vad vill du ha för användarnamn?> ')
        #self.__mail = input('Vad är din mail address?> ')
        #self.__user_age = int(input('Hur gammal är du?> '))

    def get_all(self):
        return self.__name, self.__user_name, self.__mail
    def Format(self, arg1, arg2):
        return """Hello {}:
        You wanted to know argument1: {}
        And argument2: {}""".format(self.__name, arg1, arg2)

class Money_Person(Person):
    __money = None

    def __init__(self,  wealth, name, user_name, mail, age):
        self.__money = wealth
        super().__init__(name, user_name, mail, age)

    def get_wealth(self):
        return self.__money ,self.get_name

    def set_wealth(self, amount):
        self.__money = amount


print("""Hej! Välkommen till ett litet person program!
Nu ska du få skapa ett konto""")

p1 = Money_Person(1000, 'Åke', 'Aje', 'sebastia@asdf.co m',22)
print(p1.__dict__)
