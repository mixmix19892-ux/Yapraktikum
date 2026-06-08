from datetime import datetime

print('Привет')  # Импортируйте необходимые модули.


def validate_record(name: str, birthdate: str) -> bool:
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(birthdate, "%d.%m.%Y")
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birthdate}')
        return False


def process_people(entries: list[tuple]) -> dict:
    # Объявите счётчики.
    good_count = 0
    bad_count = 0

    # Распакуйте кортежи из полученного списка entries.
    # Каждую пару значений передайте в validate_record(),
    # чтобы проверить корректность формата даты рождения.
    for i, j in entries:
        validate_record(i, j)

    # В зависимости от результата проверки увеличьте один из счётчиков.
        if validate_record(i, j) is True:
            good_count += 1
        else:
            bad_count += 1
        # Верните словарь.
    return dict(zip(['good', 'bad'], [good_count, bad_count]))


data = [
    ('Акакій Башмачкинъ',    '23 марта 1791 года'),
    ('Яков Степанов', 'Двадцать шестое июля 1971'),
    ('Потап Алексеев', '16.09.1990'),
    ('Евгений Женин', '5 декабря 1984'),
    ('Кондрат Александров', '18.01.1994')
] 
statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')
