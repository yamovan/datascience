# title Текст заголовка по умолчанию
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число за минимальное число попыток
"""

import numpy as np

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток
    """

    count = 0
    lst_num = list(range(1, 101))

    while True:
        count += 1
        predict_number = int(np.mean(lst_num))
        half = round((len(lst_num))/2)
        if number == predict_number:
            break # выход из цикла, если угадали
        elif predict_number > number:
            lst_num = lst_num[half:]  
        else:
            lst_num = lst_num[:half]
            
        
    return count

print(random_predict(1000))