import numpy as np

def random_predict(number):

    count = 0
    start = 1
    end = 100

    while True:
        count+=1
        predict_number = (start + end)//2 #первое предположение - среднее число в интервале
        if number == predict_number:
            break
        elif number > predict_number:#если предполагаемое число меньше загаданного, интервал угадывания начинается уже не с 1,
            # а c предположенного числа
            start = predict_number
        elif number < predict_number:
            end = predict_number
    return count
    


def score_game(random_predict):

    count_ls = []

    random_array = np.random.randint(1, 100, size = (1000)) #загадали список числел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses  the  number  for: {score} attempts")
    return score
    
score_game(random_predict)