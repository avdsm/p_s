# students = ['Aro', 'Baytal', 'Vazgen']
# print(students[1:])  # выводит от первого до конца
# students.append('Marus') # добавляет в конец сптска
# print(students)
# students.remove('Aro') # Удаляет первый встретившися индекс
# print(students)
# del students[1]
# print(students)
# print(len(students))  # возвращает длину списка
# students.insert(1, 'Narek')  # ставит в первый индекс
# students.append('Narek')
# students.append('Maksim')
# print(students)
# print(students.index('Narek', 2)) # искать начиная со 2-го индекса
# print(students.index('Narek', students.index('Narek') + 1)) # искать начиная со 2-го индекса
# -------------
# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8]
# a.extend(b)
# print(a)
# x = a.pop() # Вырезает последенне значение в списке и передает иксу
# # можно задать индекс, что забрать
# print(x)
# print(a)
# del a[-1] # удалить последнее значение
# print(a)
# ---------------
# a = [27, 1, 5, 16, 2, 14, 3, 5, 4, 5]
# print(a)
# b = sorted(a) # значение а не меняется
# print(b)
# d = sorted(a, reverse=True)
# print(d)
# print(a)
# a.sort() # значение а меняется
# print(a)
# ###############
# for i in range(len(a)):
#     print(a[i])

# for i in a:   # На месте i поочередно использует значения а
#     print(i)

squares = [x**2 for x in range(1, 11)]
print(squares)

