def square(side):
    area = side * side
    return round(area)


side_length = 4.7


area_result = square(side_length)
print(f"Площадь квадрата со стороной {side_length} равна {area_result}")
