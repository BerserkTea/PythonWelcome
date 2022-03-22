# Подсчитать сумму цифр в вещественном числе.
number = 15.12
stringnumber = str(number)
liststring = list(stringnumber)
for i in liststring:
    if i == ".":
        liststring.remove(i)

summOfDigits = 0
for j in liststring:
    summOfDigits += int(j)

print(liststring)
print(summOfDigits)
