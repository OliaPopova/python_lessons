import random

a= [random.randint(1,10) for i in range(6)]
result= [a[i]*a[-i-1] for i in range(len(a)//2+len(a)%2)]
print(a)
print(result)
