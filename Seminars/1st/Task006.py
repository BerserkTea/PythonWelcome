# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

number_of_day = int(input('Введите номер дня недели: '))
r = range(0, len(week)+1)
if 0<number_of_day <= 7:
    for i in r:
        if number_of_day == i:
            print(week[number_of_day - 1])
            if number_of_day == 6 or number_of_day == 7:
                print('Weeekend')
else:
    print('Число вне диапазона!')
