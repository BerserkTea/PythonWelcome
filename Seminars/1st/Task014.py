# Подсчитать сумму цифр в вещественном числе.
number = 51.1245646
print(type(number))
stringnumber = str(number).replace(".","")
# number_1= int(stringnumber)
# print(number_1)
# liststring = list(stringnumber)
# deleted_items = [",",".","-"]
# # for i in liststring:
# #     if i == ".":
# #         liststring.remove(i)
# stringnumber.remove(","or".")
# newstring=stringnumber.replace(",","")
number = 51.1245646
print(type(number))
stringnumber = str(number).replace(".","")
print (stringnumber)
summOfDigits = 0
for i in stringnumber:
    summOfDigits += int(i)
print(stringnumber)
print(summOfDigits)
