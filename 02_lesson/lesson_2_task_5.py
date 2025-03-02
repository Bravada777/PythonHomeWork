def month_to_season(x):
    if x in [1, 2, 12]:
        return "зима"
    elif x in [3, 4, 5]:
        return "весна"
    elif x in [6, 7, 8]:
        return "лето"
    elif x in [9, 10, 11]:
        return "осень"
    else:
        return "укажите правильный номер месяца"


number = int(input('введите номер месяца: '))
print(month_to_season(number))
