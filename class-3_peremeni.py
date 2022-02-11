# Boolean (Bool)
a = True
b = False

'a'.islower()  # True
'A'.islower()  # False
"Test".islower()  # False

# print('Test'.isupper())  # False
# print('Test'.istitle())   # True

'This Is A Test'.istitle()  #  True
'This Is a Test'.istitle()  #  False

'test'.isalpha()  # #  True /  В тексте должны быть только буквы
'test123'.isalpha()  # #  False
'12345'.isnumeric()  # True / В тексте должны быть тольок цифры
'test123'.isnumeric()  # #  False
'test123'.isalnum()  # #  True / Պետք է լինեն և տառեր և թվեր
'test.123'.isalnum() # # False
'test 123'.isalnum() # # False

'3.22'.isdecimal() # # FAlse  /
' '.isspace()  #  # True  / Должен быть только пробел
'tgtg 12'.isspace()  #  # False
# ##############
age = input()
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

if not age > 18:  # # Истина если age меньше 18, и ложь, если больше
