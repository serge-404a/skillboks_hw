user_string = input("Введите строку: ")
number = int(input("Введите номер символа: "))
work_string = list(user_string)
# symbol = work_string[number - 1]
# left_symbol = work_string[number - 2]
# right_symbol = work_string[number]
print(work_string[number - 1])
# print("left_symbol ", left_symbol)
# print("right_symbol", right_symbol)

if work_string[number - 1] == work_string[number - 2] and work_string[number - 1] == work_string[number]:
    print("Все символы равны")
elif work_string[number - 1] == work_string[number - 2] or work_string[number - 1] == work_string[number]:
    print("Есть один такой же символ")
else:
    print("Таких символов нет")
