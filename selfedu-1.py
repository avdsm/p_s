# Задание к уроку Selfedu Python 3 #7:
# строки - сравнения, срезы строк, базовые функции str, len, ord, in

slovo = input('Вводите строку для поиска: ')
sup_st = input("Водите символы, которые следует удалить: ")
# Считаем количество вхожденрй подстроки "sup_st" в строку "slovo"
counter = slovo.count(sup_st)

if slovo.find(sup_st) != -1:
    # Заменяем в строке символы подстроки на пустые символы и записываем в переменной "rezult_slovo"
    rezult_slovo = slovo.replace(sup_st, '')
    print('\n' f'Длина заданой строки состовляет {len(slovo)} символа.' '\n' f'"{sup_st}" в строке встречался {counter} раз. После удаления получили строку "{rezult_slovo}".')
else:
    print('\n'f'Символы "{sup_st}" в строке "{slovo}" не найдены!')
# Копирум слово в обратно порядке
slovo_rev = slovo[::-1]
# проверяем полиндромоне слово
if slovo == slovo_rev:
    print(f'Строка "{slovo}", ЕСТЬ полиндромоне слово.')
else:
    print(f'Строка "{slovo}", НЕ полиндромоне слово.')

# ######################
print('##########################')
predlozhenie = input('Вводите предложение, которе надо разбивать на слова! ')
result_1 = predlozhenie.split(' ')
for i in range(len(result_1)):
    print(result_1[i])