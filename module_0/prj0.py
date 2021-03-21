def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
'''Изначально хотел, чтобы функция сначала выяснила совпадает ли десяток, а потом единицы,
  что даст максимальное кол-во угадываний = 18 и среднее 9 но реализовать не получилось
  Можно попробовать добавить больше шагов(отрезать большие куски 50,20,15 итд и уже после подкручивать'''
    count = 1
    predict = np.random.randint(1,101)
    while num != predict1:
        if num - predict1 >10: #Если разница больше 10, значит predict1 можно увеличить
                predict1 += 10
                count += 1
        elif num - predict1 <=10: #если разница меньше 10, значит можно крутить по 1
            if num == predict1: #если угадали
                break
            elif num > predict1: #подкрутка по 1
                predict1 += 1
                count += 1
            elif num < predict1: #подкрутка по 1
                predict1 -= 1
                count += 1
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)
