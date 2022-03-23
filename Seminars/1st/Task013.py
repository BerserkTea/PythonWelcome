# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
str1 = "Мультики» — году году году роман Михаила Елизарова, изданный в 2010 году издательством АСТ."
str2 = "году"
def findHowMuch (a,b):
    counter = 0
    for i in a.split():
        # print(str(i))
        if i.find(b) != -1:
            counter+=1
    return counter
print (findHowMuch(str1,str2))

print(str1.count(str2))