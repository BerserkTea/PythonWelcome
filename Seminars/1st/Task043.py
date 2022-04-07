# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list_to_analize = [1, 2, 3, 5, 1, 5, 3, 10, 11,12 ,2 ,10 ,15]
list_unicum = []
for number in list_to_analize:
    counter=0
    for i in range(len(list_to_analize)):
        if number == list_to_analize[i]:
            counter+=1
    if counter==1:
        list_unicum.append(number)
        
print(list_unicum)


lst = [1, 2, 30, 3, 5, 11, 1, 5, 3, 10]
lst = [i for i in lst if lst.count(i) == 1] # lst.count(i) == 1 - количество вхождений элементов в списке равное одному
print(lst)
