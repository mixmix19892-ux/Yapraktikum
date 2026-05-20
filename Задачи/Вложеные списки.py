import random
# 1. Создание списка списков:
plot = 3
bed = 3
harvest = [[random.randint(5, 20) for i in range(plot)] for i in range(bed)]
  # Примените list comprehension.




# # 2. Функция для подсчёта общего урожая:
def total_harvest(harvest):
    summ_harvest = 0
    for element in harvest:
        summ_harvest += sum(element)
    return summ_harvest



# # 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest):
    average = [sum(element) / len(harvest) for element in harvest]
    return average


# # Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))