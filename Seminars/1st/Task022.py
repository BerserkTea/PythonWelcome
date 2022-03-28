# 22.Найти сумму чисел списка стоящих на нечетной позиции

spisok_1 = [1,123,3,11,11,6,7,8,9,10,11,12,12,14,15,16,17,18,19]
summary = 0
# for i in range(1,len(spisok_1),2):
for i in range(len(spisok_1)):
    if i%2!=0:
        summary+=spisok_1[i]
print (summary)