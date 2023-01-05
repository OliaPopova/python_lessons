# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input("Введите десятичное число для преобразовывания в двоичное:\n"))
binarynumber = ""
while number != 0:
    binarynumber = str(number % 2) + binarynumber
    number //= 2
print(f'{number} ->{binarynumber}')
