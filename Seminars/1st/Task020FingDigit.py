# 20.Определить, присутствует ли в заданном списке строк, некоторое число

# somestring = "Приветики пистолетики"
# string_list = ["dads", "123", "dad2312s", "dadsd21s",
#                "dadsgfgd", "dadsaa", "dad", "das", "dds", "123dads"]


# if 123 in string_list: print("Все хорошо")
# else: print("Все хорошо, но не очень")


# what_to_find = input("Введите искомое число ")
# flag = True
# for i in string_list:
#     if flag == False:
#         break
#     elif i == what_to_find:
#         print(f"Искомое число {what_to_find} есть в списке")
#         flag = False
# if flag==True:
#     print(f"Искомое число {what_to_find} отсутсвует в списке")


# print(type(string_list))
somestring = "Приветики пистолетики"
string_list = ["dads", "fhj", "dad2312s", "dadsd21s",
               "dadsgfgd", "dadsaa", "6545", "das", "dds", "123dads"]

for i in string_list:
    if i.isdigit():
        print(f'Все окей, число есть {i}')
        exit()
print("ничего не найдено")