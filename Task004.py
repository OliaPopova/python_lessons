# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a= int(input('a = '))

def checkinput(a):
    if a>4 or a<1:
        print('Введите число, которое может обозначать координатную четверть! (от 1 до 4)')
        a= int(input('a = '))
    return a

def quarter(a):
    if a==1:
        print(f'x>0 y>0 ')       
        
    if a==2: 
        print(f'x<0 y>0') 

    if a==3: 
        print(f'x<0 y<0') 
    
    if a==4: 
        print(f'x>0 y<0') 

a=checkinput(a)
quarter(a)



