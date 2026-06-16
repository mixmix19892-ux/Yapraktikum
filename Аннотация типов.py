"""Lalala."""


def find_max_even_number(value):
    """Находит максимальное чётное число в списке."""
    CurrentMax = 0

    for b in value:
        if b % 2 == 0:
            CurrentMax = max(b, CurrentMax)
    return CurrentMax


max_even = find_max_even_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_even_number() другие списки:
print(f"Максимальное чётное число: {max_even}")
