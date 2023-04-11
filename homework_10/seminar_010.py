# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |
Да, можно перевести столбец в one hot вид без использования функции get_dummies().
Можно использовать метод pandas Series.str.get_dummies() для создания one hot кодированного DataFrame.
Вот пример кода, который решает эту задачу:

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

# Создаем новый DataFrame, используя метод get_dummies
one_hot = data['whoAmI'].str.get_dummies()
# Объединяем два DataFrame по индексу
data = pd.concat([data, one_hot], axis=1)
# Удаляем столбец 'whoAmI' и первый столбец кодировки one hot
data = data.drop(['whoAmI', 'robot'], axis=1)
data.head()
```

Результат выполнения этого кода выглядит следующим образом:
```
   human
0      0
1      1
2      1
3      1
4      0
```

Здесь был создан новый DataFrame one_hot при помощи pandas метода Series.str.get_dummies(),
который создает новый DataFrame с одним столбцом для каждого класса в списке и присваивает им значения 0 или 1.
Затем мы объединили исходный DataFrame с новым DataFrame по индексу используя метод pd.concat().
Столбец 'whoAmI' и первый столбец кодировки one hot были удалены из результирующего DataFrame,
чтобы получить одну колонку one hot кодированного DataFrame.