# f = open("1.txt", "r")
# print(f.read())
# f.close()
# with open("1.txt", "a") as f:
#      i_text = input("Вводите текст для записи в файле: ")
#      f.write("\n" + i_text)
#
# with open("1.txt", "r") as f:
#     print(f.read())
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except ZeroDivisionError:
    print('Нельзя делить на 0 !!!!')
finally:
    if b == 0:
        print("Выводите данные заново!")







