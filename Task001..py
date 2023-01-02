# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a= int(input('a = '))

def checkinput(a):
    if a>7 or a<1:
        print('Введите число, которое может обозначать день недели! (от 1 до 7)')
        a= int(input('a = '))
    return a


def DayOfTheWeek(a):
    if 1<=a<=5:
        print(f'{a} -> нет')       
        
    else: 
        print(f'{a} -> да') 

a=checkinput(a)
DayOfTheWeek(a)