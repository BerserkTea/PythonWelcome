# Дан список чисел.
# Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

# some_list = [1, 5, 2, 3, 4, 6, 1, 7]

# i=0
# while i<(len(lst)-1):
#     if lst[i]<lst[i+1]:
#         lst2.append(lst[i])
#     i+=1
#     # else:
#     #     # lst.remove(lst[i])
#     #     continue
# print(lst2)

import random
lst=[1, 5, 2, 3, 4, 6, 1, 7]
lst2 =[]
index = random.randrange(len(lst))
# index = 5
print(index)
lst2.append(lst[index])
if index <= len(lst)-2:
    index+=1
    for index in range(index,len(lst)-1):
        if lst2[-1]<lst[index]<lst[index+1]:
            lst2.append(lst[index])
        elif lst[index]>lst2[-1]:
                lst2.append(lst[index])
if lst[-1]>lst2[-1]:
    lst2.append(lst[-1])
print(lst2)