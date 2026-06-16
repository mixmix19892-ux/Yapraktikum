def print_multiplication_table():
    # Напишите код, который напечатает таблицу умножения.
    for v1 in range(1, 10):
        for v2 in range(1, 10):
            print(f'{v1} * {v2} = {v1 * v2}')
        print('----------')



print_multiplication_table()