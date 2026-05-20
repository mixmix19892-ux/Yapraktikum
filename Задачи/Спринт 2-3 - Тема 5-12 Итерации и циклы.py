def print_pack_report(starting_value):
    # Объявите диапазон от starting_value до 1 включительно
    # и переберите его в цикле:
    for number in range(starting_value, 0, -1):
        # Проверьте, делится ли текущий элемент
        # на 3, на 5 и на 3 и 5 одновременно.
        # В зависимости от результата проверки
        # напечатайте нужную фразу
        if number % 3 == 0:
            if number % 5 == 0:
                print(f'{number} - расфасуем по 3 или по 5')
            else:    
                print(f'{number} - расфасуем по 3')
        elif number % 5 == 0:
            print(f'{number} - расфасуем по 5')
        else:
            print(f'{number} - не заказываем!')


print_pack_report(31)