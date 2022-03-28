from tkinter import *
from decimal import *

#Создаем окно приложения  — объект Tk с заголовком Calculator. 
#Во вложенном кортеже buttons будут храниться обозначения для кнопок.
#В список stack будем добавлять введенные числа и операции, которые надо совершить.
#activeStr предназначен для хранения набираемого числа.
root = Tk()
root.title('Калякулятор')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )


activeStr = ''
stack = []

# Функция calculate получает из списка stack операнды и операцию которую над ними надо произвести.
# Результат отображается в надписи label.
# Получать из списка строки будем с помощью метода pop.
def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

#В функции click выполняется обработка нажатой клавиши. В качестве ее аргумента передается текст, отображаемый на кнопке, которую нажали. 
#Хотелось бы хранить вводимое значение прямо в надписи, а не создавать для этого отдельную переменную.
#Но так не получается из-за алгоритма работы. После того как посчитан результат, он записывается в надписи.
#При попытке после этого начать вводить новое число, оно бы дописывало прежний результат.
#В списке с операторами и командами для калькулятора не обязательно их будет 3.
#Но при обработке с помощью метода pop, будут рассматриваться 3 последних введенных значения.
#А после проведения расчета список очистится. Далее в него добавляется полученный результат, на случай если пользователь нажмет на калькуляторе клавишу операции сразу,
#а не будет вводить новое число.
def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

# Внешний вид
# Теперь займемся оформлением внешнего вида калькулятора и зададим обработку нажатия кнопок.

label = Label(root, text='0', font=("Times New Roman", 21, "bold"), width=35)
# Создаем надпись для вывода набираемых значений и результатов.
label.grid(row=0, column=0, columnspan=4, sticky="nsew")
# Если функция grid не будет вызвана, текст не будет отображаться.
button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
# В цикле создаем кнопки.
# Расположение кнопок и надписи осуществляется в табличном виде с помощью упаковщика grid.
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],font=("Times New Roman", 15),
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
# И в завершении запускаем цикл обработки событий mainloop.
# mainloop. Эта функция вызывает бесконечный цикл окна, поэтому окно будет ждать любого взаимодействия с пользователем, пока не будет закрыто.
#У надписи выставлена ширина 35, для того, чтобы оформление кнопок подстраивалось под надпись.
#И в результате кнопки при этом значении лучше выглядят.
#Для того, чтобы кнопки правильно работали, пришлось для каждой из кнопок создать свою функцию с помощью lambda.