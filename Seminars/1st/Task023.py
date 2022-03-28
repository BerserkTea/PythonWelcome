# 23.Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

def MultPair(listMultPair):
    listAdd = []
    if (len(listMultPair) % 2 == 0):
        for i in range(0, len(listMultPair)//2):
            listAdd.append(listMultPair[i] * listMultPair[len(listMultPair)-1-i])
    else:
        for i in range(0, (len(listMultPair)+1)//2):
            listAdd.append(listMultPair[i] * listMultPair[len(listMultPair)-1-i])
    return listAdd


list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 4, 5, 6, 7]
print(MultPair(list1))
print(MultPair(list2))