import numpy as np

def game_core_v3(number):
    ''' На каждом шаге выбирается случайное число из заднного диапазона поиска.
        Границы даипазона изменяются в зависимости в зависимости от того, больше проверяемое число или меньше нужного.
        Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    low_limit = 1   # нижняя граница диапазона поиска
    up_limit = 100  # верхняя граница диапазона поиска
    predict = np.random.randint(low_limit, up_limit + 1 )
    while number != predict:
        count += 1
        if number > predict:
            low_limit = predict + 1
            predict = np.random.randint(low_limit, up_limit + 1)
        elif number < predict:
            up_limit = predict - 1
            predict = np.random.randint(low_limit, up_limit + 1)
    return count # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

# запускаем
score_game(game_core_v3)


