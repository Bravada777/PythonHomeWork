lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Отфильтруем элементы, которые меньше 30 и делятся на 3
filtered_list = [num for num in lst if num < 30 and num % 3 == 0]

# Вывод результатов
print(filtered_list)
