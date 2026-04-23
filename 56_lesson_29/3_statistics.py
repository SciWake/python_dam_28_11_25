import statistics

# Набор данных
data = [12, 15, 14, 10, 1, 1, 1, 18, 17, 15, 15, 14, 200]

# Средние значения
print("Арифметическое среднее:", statistics.mean(data))
print("Геометрическое среднее:", statistics.geometric_mean(data))
print("Гармоническое среднее:", statistics.harmonic_mean(data))

# Характеристики на отсортированном наборе
print("Отсортированный список:", sorted(data))
print("Медиана:", statistics.median(data))
print("Мода:", statistics.mode(data))

# Квантильные значения (делим на 4 части — квартиль)
print("Квартили:", statistics.quantiles(data, n=4))

# Измерения разброса
print("Стандартное отклонение:", statistics.stdev(data))
print("Дисперсия:", statistics.variance(data))
