import os
#with open('100lines.txt', 'w+') as f:
    #for i in range(100):
        #f.write(str(i+1) + '\n')
    #print(f.tell())

#with open('100lines.txt', 'r+') as p:
    #p.read(10)
    #print(p.tell())



# WITH WHILE LOOP
#i = -1
#with open('100lines.txt', 'r') as f:
    #i = -1
    #while f.tell() != i:
        #i = f.tell(
        #print(f.readline(), end="")

with open('100lines.txt', 'r') as x:
    with open('100lines2.txt', 'w') as y:
        for i in x:
            print(i, end='')
