# 21.Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# spisok_2 = "привет малыш я карлсон полетели на крышу"


spisok_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
stroka_1 = "йцу"
count = 0
print(spisok_1.count(stroka_1))
if spisok_1.count(stroka_1) <2:
    count = -1
else:
    for i in range(len(spisok_1)):
        if spisok_1[i] == stroka_1:
            count+=1
            if count ==2:
                count = i
                break
print(f'Искомое {stroka_1}, ответ {count}')


# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe","qwe","qwe"]
# string1 = "qwe"

# if list1.count(string1) < 2:
#     print("Второго вхождения нет")
# countString = 0
# countPos = 0
# for i in list1:
#     if string1 in i:
#         countString += 1
#     if countString == 2:
#         print(countPos)
#     countPos += 1