def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return year % 400 == 0
    else:
        return True


test_year = 2024


result = is_year_leap(test_year)
print(f'Год {test_year}: {result}')
