a= [int(input(f"Введите {i} координату точки А : ")) for i in "XY"]
b= [int(input(f"Введите {i} координату точки B : ")) for i in "XY"]
mylist=list(zip(a,b))

result=sum([(elem[1]-elem[0])**2 for elem in zip(a,b)])**0.5

print(round(result, 2))