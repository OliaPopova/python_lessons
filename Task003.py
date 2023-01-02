# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x= int(input('x = '))
y= int(input('y = '))


def checkCoordinates(x,y):
    text = 4
    if x > 0 and y > 0:
        text = 1
    elif x < 0 and y > 0:
        text = 2
    elif x < 0 and y < 0:
        text = 3
    print(f"x={x}; y={y} -> {text}")


checkCoordinates(x,y)


