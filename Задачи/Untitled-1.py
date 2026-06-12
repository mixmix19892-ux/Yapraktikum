def average_price(*args):
        if not args:
            return 0
        return sum(args) / len(args)


retail_prices = [1, 2, 3]
print(average_price(*retail_prices))