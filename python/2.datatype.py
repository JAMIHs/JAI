from dataclasses import replace
import math
import random


print(1)
print(1.1)
print(1+1)
print(2-1)
print(2*2)
print(6/2)
print(math.pow(3,2))
print(pow(3,2))
print(random.random()*100)

#String
print(len('Hello'))
print('Hell'.replace('Hell','Hello'))
print('''
    Hello
    World
''')
#List
member = ['egoing','duru','teaho']
print(member[0])
print(len(member))

print(random.choice(member))
score = [100,200,300]
print(sum(score))