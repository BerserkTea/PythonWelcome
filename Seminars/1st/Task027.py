# 27.Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

what_to_analise_list = input('введите через пробел строку чисел ').split()
list1 = [3, 2, 8, 5, 10, 6, 123, 4254,12314,11 ,2134]
print(list1)
print(max(list1))
print(min(list1))
print(max(what_to_analise_list))