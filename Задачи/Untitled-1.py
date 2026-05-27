import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%M-%d'

goods = {}


def add(items, title, amount, expiration_date=None):
    
    if title not in items:
        items[title] = []

    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    else:
        expiration_date
        
    list.append(items[title], {'amount': amount, 'expiration_date': expiration_date})

    
    print(items)



# add({}, 'Яйца Фабрики №1', 4, '2023-07-15')


def add_by_note(items, note):
    separator = str.split(note, ' ')
    separator_date = str.split(separator[-1], '-')
    if len(separator_date) == 3:
        expiration_date = note[-1]
    else:
        continue

    separator_amount = Decimal(separator[-2])
    
    print(separator)
    print(separator_date, type(separator_date))
    print(separator_amount, type(separator_amount))

add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15')