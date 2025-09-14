def month_to_season(month):
    if month > 12 or month < 1:
        print("Нет такого месяца")
    elif month == 1 or month == 2 or month == 12:
        print("Зима")
    elif month == 3 or month == 4 or month == 5:
        print("Весна")
    elif month == 6 or month == 7 or month == 8:
        print("Лето")
    else:
        print("Осень")


month = int(input("ВВедите месяц: "))
month_to_season(month)
