# Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
# загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# выбор данных, где кол-во людей от 0 до 500
data_filtered = data[(data['population'] > 0) & (data['population'] <= 500)]

# определение средней стоимости дома в выборке
mean_price = data_filtered['median_house_value'].mean()

# вывод результата
print(f"Средняя стоимость дома с количеством людей от 0 до 500: ${mean_price:.2f}")

# В результате выполнения кода будет выведено значение средней стоимости дома с количеством людей от 0 до 500

# Узнать какая максимальная households в зоне минимального значения population
# загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# определение минимального значения population
min_pop = data['population'].min()

# выбор данных, где population равна минимальному значению
data_filtered = data[data['population'] == min_pop]

# определение максимального значения households в выборке
max_households = data_filtered['households'].max()

# вывод результата
print(f"Максимальное значение households в зоне с минимальным значением population: {max_households}")

# В результате выполнения кода будет выведено максимальное значение households в зоне с минимальным значением population.
