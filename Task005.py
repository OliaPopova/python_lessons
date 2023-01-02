# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def calculateLengthSegment(x1, x2, y1, y2):
    lengthSegment = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
x1= int(input('x1= '))
y1= int(input('y1= '))
print("Введите координаты точки В")
x2= int(input('x2= '))
y2= int(input('y2= '))

print(f"Длина отрезка: {format(calculateLengthSegment(x1, x2, y1, y2), '.2f')}")