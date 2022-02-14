# Boolean (Bool)
# a = True
# b = False

'a'.islower()  # True
'A'.islower()  # False
"Test".islower()  # False

# print('Test'.isupper())  # False
# print('Test'.istitle())   # True

<<<<<<< HEAD
'This Is A Test'.istitle()  # True
'This Is a Test'.istitle()  # False
=======
'This Is A Test'.istitle()  #  True
'This Is a Test'.istitle()  #  False
>>>>>>> origin/main

'test'.isalpha()  # #  True /  В тексте должны быть только буквы
'test123'.isalpha()  # #  False
'12345'.isnumeric()  # True / В тексте должны быть тольок цифры
'test123'.isnumeric()  # #  False
'test123'.isalnum()  # #  True / Պետք է լինեն և տառեր և թվեր
<<<<<<< HEAD
'test.123'.isalnum()  # # False
'test 123'.isalnum()  # # False
=======
'test.123'.isalnum() # # False
'test 123'.isalnum() # # False
>>>>>>> origin/main

'3.22'.isdecimal() # # FAlse  /
' '.isspace()  #  # True  / Должен быть только пробел
'tgtg 12'.isspace()  #  # False
# ##############
<<<<<<< HEAD
# age = input()
# if age.isnumeric():
#     print("Ok, accepted " + age)
#     age = int(age)
#     if age >= 18:
#         print('You can bay alcogol')
#     elif age >= 16:
#         print('You can bay BEAR')
#     else:
#         print('Sictiran cax!')
# else:
#     print('You are entered incorrect age')

#if not age > 18:  # # Истина если age меньше 18, и ложь, если больше

# ##################################
# x_num = input()
# if x_num.isnumeric():
#     x_num = int(x_num)
#     if x_num % 2 != 0:
#         print("Kent")
#     if 2 <= x_num < 5:
#         print("ZZZ")
#     elif 6 <= x_num <20:
#         print("Kent")
#     else:
#         print("ZZZ")
# else:
#     print('You are entered incorrect data')

# ############## Короткий IF
# x_num = input()
# x_num = int(x_num)
# print("Kent" if x_num % 2 != 0 and (2 <= x_num < 5 or x_num > 20) else "ZZZ")

# ########## Цикл FOR  # Старт, Стоп, Шаг
# for i in range(4, 26, 4):
#     print(i)
# #########
n = 2
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')

# ########## Убрать переход строки
n = 5
for i in range(5):
    print(i, end=" ")


=======
age = input("Please enter data: ")
if age.isnumeric():
    print("Ok, accepted " + age)
    age = int(age)
    if age >= 18:
        print('You can bay alcogol')
    elif age >= 16:
        print('You can bay BEAR')
    else:
        print('Sictiran cax!')
else:
    print('You are entered incorrect age')

#if not age > 18:  # # Истина если age меньше 18, и ложь, если больше
>>>>>>> origin/main
