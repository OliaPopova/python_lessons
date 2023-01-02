# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x= int(input('x = '))
y= int(input('y = '))
z= int(input('z = '))


def checkPredicate(x,y,z):
    a = not (x or y or z)
    b = not x and not y and not z
    result = a == b
    return result

print(checkPredicate(x,y,z))
