def analyze_results(list_of_dicts: list[dict[str, int]]):
    # Получите названия всех команд и отсортируйте их по алфавиту.
    scores = {}

    for dict in list_of_dicts:
        for key in dict:
            scores[key] = 0

    for dict in list_of_dicts:
        for key, value in dict.items():
            scores[key] += value

    winner = None
    winner_score = 0

    for key, value in scores.items():
        if winner_score < value:
            winner_score = value
            winner = key

    

    print('Команды, участвовавшие в чемпионате:')

    for key in sorted(scores):
        print(f'* {key}')

    print(f'В чемпионате победила команда {winner} с результатом {winner_score} баллов')


    


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)