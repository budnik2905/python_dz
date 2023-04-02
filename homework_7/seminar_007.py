# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам
vowels = 'aeiouyAEIOUY'

poem = input("Введите стихотворение Винни-Пуха: ")

phrases = poem.split()

prev_vowel_count = None
for phrase in phrases:
    # Подсчет числа гласных букв в фразе
    vowel_count = sum(1 for char in phrase if char in vowels)
    if prev_vowel_count is not None and prev_vowel_count != vowel_count:
        print("Пам парам")
        break
    prev_vowel_count = vowel_count
else:
    print("Парам пам-пам")
# второй вариант
s = input().split()  # считываем стихотворение и разбиваем на слова
syllables = []  # список для хранения количества слогов в каждой фразе
for word in s:
    syllables.append(word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count(
        'u'))  # подсчитываем количество гласных букв в слове и добавляем в список
if len(set(syllables)) == 1:  # если все элементы списка равны друг другу
    print("Парам пам-пам")
else:
    print("Пам парам")

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание:
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печать заголовка таблицы
    print("  ", end="")
    for j in range(1, num_columns + 1):
        print(j, end=" ")
    print()

    # Печать строк таблицы
    for i in range(1, num_rows + 1):
        print(i, end=" ")
        for j in range(1, num_columns + 1):
            # Вычисление и печать значения на пересечении строки i и столбца j
            value = operation(i, j)
            print(value, end=" ")
        print()


# Пример использования
print_operation_table(lambda x, y: x * y)
# второй вариант
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = ''
        for j in range(1, num_columns + 1):
            row += str(operation(i, j)) + ' '
        print(row.strip())


# пример использования
print_operation_table(lambda x, y: x * y)
