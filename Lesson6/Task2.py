import random

a=[random.randint(1,10) for i in range(6)]
print(a)
result = sum([value for i,value in enumerate(a) if i%2==1])
print (result)

