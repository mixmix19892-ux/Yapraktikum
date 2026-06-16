"""lalala"""


def find_max_even_number(values: list[int]) -> int:
    """Находит максимальное чётное число в списке положительных целых чисел."""
    current_max = 0
    for value in values:
        if value % 2 == 0:
            current_max = max(value, current_max)
    return current_max


max_even = find_max_even_number([1, 2, 3, 4, 5])
print(f'Максимальное чётное число: {max_even}')
