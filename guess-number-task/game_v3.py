import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    upper_limit = 100
    lower_limit = 0
    while upper_limit >= lower_limit:
        count += 1
        predict = (upper_limit+lower_limit)//2

        if predict == number:
            return count

        elif number > predict:
            lower_limit = predict+1

        else:
            number < predict
            upper_limit = predict-1
    return count


print(game_core_v3())

