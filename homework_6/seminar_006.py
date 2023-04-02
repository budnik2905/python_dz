# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = []  # пустой список, который будем заполнять элементами

for i in range(n):
    element = a1 + i * d  # вычисляем текущий элемент прогрессии
    progression.append(element)  # добавляем его в список

print("Элементы прогрессии: ")
for element in progression:
    print(element)
# второй вариант
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = []

for i in range(n):
    progression.append(a1 + i * d)

print("Массив элементов арифметической прогрессии: ")
for i in progression:
    print(i)
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
arr = [1, 5, 8, 10, 3, 7, 2]
min_val = 3
max_val = 7
indexes = get_indexes(arr, min_val, max_val)
print(indexes)  # [1, 4, 5, 6]


# второй вариант
def find_indexes(arr, min_val, max_val):
    indexes = []
    for i, val in enumerate(arr):
        if min_val <= val <= max_val:
            indexes.append(i)
    return indexes
