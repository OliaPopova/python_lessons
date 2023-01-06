# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_of_element(mylst):
    summa = 0
    for i in range(len(mylst)):
        if i % 2 != 0:
            summa += mylst[i]
    print(f"Сумма равна: {summa}")

mylst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_of_element(mylst)


