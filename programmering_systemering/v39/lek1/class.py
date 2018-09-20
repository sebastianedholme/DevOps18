class Person():
    pass

#me = Person()
#me.name = 'Sebastian'
#me.name = 'The dude'
#me.age = 23
#me.old = True
#me.young = False
#print(me.__dict__)
#print(getattr(me, 'energy', 100))

sebastian = Person()
sebastian.name = 'Sebastian'
sebastian.age = 32
sebastian.email = 'sebastian.edholm@gmail.com'
print(sebastian.__dict__)


## Get attr ersötter bara värdet om inget värde redan finns.
def f(x):
    f.counter = getattr(f,'counter', 0) + 1
    return 'Monthy Python'

for i in range(20):
    f(i)

print(f.counter)

print(getattr(sebastian, 'name', 2))

