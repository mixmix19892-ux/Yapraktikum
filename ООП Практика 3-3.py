class Customer:
    def __init__(self, name: str):
        self.name = name
        self.__discount = 10

    def set_discount(self, new_value: int):        
        if new_value < 80:
            self.__discount = new_value
        else:
            self.__discount = 80

    def get_price(self, price: int) -> float:
        discount = price * self.__discount / 100
        return round((price - discount), 2)


# Проверим работу программы.
# Создаём объект покупателя:
customer = Customer('Иван Иванович')

original_price = 85

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен установить размер скидки равным 80.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)