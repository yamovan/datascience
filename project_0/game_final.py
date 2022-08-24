import numpy as np
number = np.random.randint(1, 101) # загадываем рандомное число
def random_predict(number) -> int:
    """Компьютер угадывает рандомное число из диапазона от 1 до 100 за минимальное число попыток

    Args:
        number (int, optional): Загаданное число

    Returns:
        int: Число попыток
    """
    count = 0
    min_num = 1 # минимальное число в диапазоне поиска чисел
    max_num = 100 # максимальное число в диапазоне поиска чисел

    while True:
        count += 1
        mid_num = round((min_num + max_num)/2) # среднее число в диапазоне поиска чисел
        if mid_num > number:
            max_num = mid_num # сокращаем диапазон чисел для поиска
        elif mid_num < number:
            min_num = mid_num # сокращаем диапазон чисел для поиска
        else:
            break # выход из цикла, компьютер определил загаданное число
            
    return count


print(f'Количество попыток: {random_predict(number)}')



