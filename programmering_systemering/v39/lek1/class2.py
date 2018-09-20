## 
class Person:
    def __init__(self, the_name, email, age):
        self.name = the_name
        self.email = email
        self.age = age

        if age > 30:
            self.old = True
            print('Damn you old')
        else:
            self.old = False
            print('OOuh yeah still young')

    def printall(self):
        print(self.__dict__)

class PhoneBook:
    lists = []
    def __init__(self, obj):
        self.lists.append(obj)

#my_self = Person(input("Ange ditt namn: "), input("Ange din email: "), int(input("Ange din ålder: ")))
my_self = Person('Sebastian', 'sebastian.edholm@gmail.com', 23)
ake = Person('Åke', 'ake@ake.se', 45)
my_self.printall()

my_book = PhoneBook(my_self)
my_book = PhoneBook(ake)


for i in range(len(my_book.lists)):
        print(my_book.lists[i].name)
