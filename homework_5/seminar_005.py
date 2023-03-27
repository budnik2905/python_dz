# Напишите программу на Python которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:* A = 3; B = 5 -> 243 (3⁵) A = 2; B = 3 -> 8
def power_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a, b - 1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

result = power_recursive(a, b)
print(f"{a} в степени {b} равно {result}")

# второй вариант
def power_of_number(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power_of_number(a, b // 2) ** 2
    else:
        return a * power_of_number(a, b - 1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
result = power_of_number(a, b)
print(f"{a} в степени {b} = {result}")

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a-
    else:
        return sum(a - 1, b + 1)


a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
print(sum(a, b)

#второй вариант


def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)  # a + b = (a + 1) + (b - 1)

