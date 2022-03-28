# 24.В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
max = 0.000
min = 1.000
float_spisok = [1.1, 1.2, 0, 5.002, 10.000001, 11.13, 5, 10.11, 122324.52, 0.14]

for i in range(len(float_spisok)):
    float_spisok[i]=round(float_spisok[i]%1,10)
    if float_spisok[i] !=0:
        if max<float_spisok[i]:
            max = float_spisok[i]
        if min>float_spisok[i]:
            min = float_spisok[i]
    else: continue
    print(float_spisok[i])
print(float_spisok)
print(max-min)