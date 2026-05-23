import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%M-%d'

goods = {}


def add(items:dict, title: str, amount, expiration_date=None):
    
    
    if items.get(title) is None:
        items[title] = []

    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()

    items[title].append({'amount': Decimal(amount), 'expiration_date': expiration_date})


def add_by_note(items:dict, note:str):
    split = note.split()

    try:
        if datetime.datetime.strptime(split[-1], DATE_FORMAT).date():
            expiration_date = split.pop(-1)
    except ValueError:
        expiration_date = None
    
    amount = split.pop(-1)

    title = ' '.join(split)

    add(items, title, amount, expiration_date)
    

def find(items:dict, needle:str) -> list:
    result = []
    for key in items:
        if needle.lower() in key.lower():
            result.append(key)
    return result


def get_amount(items, needle) -> Decimal:
    result_find = find(items, needle)
    total_items = Decimal(0)

    for key in result_find:
        info_products = items[key]
        for info in info_products:
            total_items += info['amount']
        
    return total_items


def get_expired(items:dict, in_advance_days=None) -> list[tuple]:
    today = datetime.datetime.now().date()

    if in_advance_days:
        today += datetime.timedelta(days=in_advance_days)

    result = []
    temp = {}

    for key, info_products in items.items():
        for info in info_products:
            expiration_date = info['expiration_date']

            if expiration_date and expiration_date > today:
                continue

            if temp.get(key) is None:
                temp[key] = info['amount']
            else:
                temp[key] += info['amount']

    for key, amount in temp.items():
        result.append((key, amount))

    return result
    

def main():
    add(goods, 'Яйца Фабрики №1', 4, '2026-05-21')
    add_by_note(goods, 'Макароны 1.5')
    add_by_note(goods, 'Яйца Фабрики №1 4 2026-05-23')

    get_amount(goods, 'Яйца Фабрики №1')

    expired = get_expired(goods, 5)

    out = find(goods, 'яйца')

    print(goods)



if __name__ == "__main__":
    main()