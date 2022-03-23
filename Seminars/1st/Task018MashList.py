# 18.Реализовать алгоритм перемешивания списка.
import random


test_spisok = [2, 124, 566, 2, 19, 16, 3, 4, 11, 784, 221, 10]
print(test_spisok)
listLenght = len(test_spisok)
for i in range(0, listLenght):
    somedigit = random.randrange(0, listLenght)
    test_spisok[i], test_spisok[somedigit] = test_spisok[somedigit], test_spisok[i]
print(test_spisok)

def mashSomeList(somelist):

    for i in range(0, listLenght):
        somedigit = random.randrange(listLenght)
        somelist[i], somelist[somedigit] = somelist[somedigit], somelist[i]
    return somelist
print(mashSomeList(test_spisok))
