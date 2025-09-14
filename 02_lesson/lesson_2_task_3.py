import math


def square(side_str):
    if '.' in side_str:
        side = float(side_str)
        result = math.ceil(side ** 2)
    else:
        side = int(side_str)
        result = side ** 2
    return result


side_str = input("Введите сторону квадрата: ")
result = square(side_str)

print(f"Площадь квадрата со стороной {side_str}: {result}")
