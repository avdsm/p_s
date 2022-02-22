# import math
#
# def calc(x):
#   return math.log(abs(12*math.sin(x)))
#
# print(calc(451))

# Еще одно решение этой задачи
my_string = input('Вводите строку для поиска: ')
sup_st = input("Водите символы, вхождение которых надо подсчитать: ")
start = -1
count = 0

while True:
    if count == 0:
        start = my_string.find(sup_st, start+1)
    elif count > 0:
        start = my_string.find(sup_st, start + len(sup_st))
    else:
        print('Ошибка!')
    if start == -1:
        if count == 0:
            print('Совпадение не найдено!')
        break
    count += 1

rezult_slovo = my_string.replace(sup_st, '')
print(f"Количество вхождений символа '{sup_st}' в строку: ", count)
if count != 0:
    print(f'Строка после удаления символов "{sup_st}" получится таким - "{rezult_slovo}"')

