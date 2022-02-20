slovo = input('Вводите строку для поиска: ')
sup_st = input("Водите символы, которые следует удалить: ")
dlina = int(len(slovo))
print(f'Длина строки сосотовляет {dlina} символов!')
rezult_slovo = ''
i = 0
if slovo.find(sup_st) != -1:
    rezult_slovo = slovo.replace(sup_st, '')
    i = 1
    for sup_st in rezult_slovo:
        i += 1
        rezult_slovo = slovo.replace(sup_st, '')
else:
    print(f'Символы "{sup_st}" в строке "{slovo}" не найдены!')


print()
print(f'''Символы "{sup_st}" в строке "{slovo}" найдены "{i}" раз. 
После удаления получили строку "{rezult_slovo}".''')
