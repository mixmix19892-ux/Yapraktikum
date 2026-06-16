def fibonacci(n):
    a = 0
    b = 1
    toggle = False # Переключатель

    yield 0

    while n > 1:
        res = a + b
        yield res

        n -= 1

        if toggle:
            a = res
            toggle = False
        else:
            b = res
            toggle = True

        
        

sequence = fibonacci(10)
for number in sequence:
    print(number)