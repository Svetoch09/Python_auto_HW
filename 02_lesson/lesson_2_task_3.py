import math


def square(side):
    area = side ** 2

    # Проверяем, является ли side целым числом
    if isinstance(side, float):
        # Если это float, округляем результат вверх
        return math.ceil(area)
    else:
        # В противном случае возвращаем обычный результат
        return area


side = float(input("Введите сторону квадрата: "))
result = square(side)


print(f"Площадь квадрата со стороной {side}: {result}")
