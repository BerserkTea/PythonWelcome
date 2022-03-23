# Подсчитать сумму цифр в вещественном числе.
number = 15.1245646
stringnumber = str(number)
liststring = list(stringnumber)
# for i in liststring:
#     if i == ".":
#         liststring.remove(i)
liststring.remove(".")
summOfDigits = 0
for i in liststring:
    summOfDigits += int(i)

print(liststring)
print(summOfDigits)
