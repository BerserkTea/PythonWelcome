# 32.Дана последовательность чисел.
# Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]


# firs_list = [1, 2, 3, 5, 1, 5, 3, 10]
# second_list = set(firs_list)
# print(second_list)


# 32.	Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list = [1, 2, 3, 5, 1, 5, 3, 10]

def number(list):
    unnumber = []
    for number in list:
        if number in unnumber:
            continue
        else:
            unnumber.append(number)
    return unnumber

print(number(list))
