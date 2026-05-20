def analyze_results(list_of_dicts):
    # Получите названия всех команд и отсортируйте их по алфавиту.
    dict = list_of_dicts[0]
    sorted_dict = sorted(dict)

    print('Команды, участвовавшие в чемпионате:')

    for key in sorted_dict:
        print(f'* {key}')

       



    


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)