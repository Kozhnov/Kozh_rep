"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0

# первоначальные границы
thirst_limit = 1
last_limit = 100

while True:
    secret_number = (thirst_limit + last_limit) // 2
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Число должно быть меньше!")
        last_limit = secret_number

    elif predict_number < number:
        print("Число должно быть больше!")
        thirst_limit = secret_number
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла

