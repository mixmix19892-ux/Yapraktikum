# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.

# def check(value):
#     if value % 3 == 0:
#         return value ** 2
#     else:
#         return 0

pows = ((value ** 2 if value % 3 == 0 else 0) for value in numbers)

# Распечатайте сумму квадратов.
print(sum(pows))
    