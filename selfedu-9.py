# Задание к уроку  https://youtu.be/ImWIDeW4GH0
list_1 = [-1, 0, 5, 3, 2]
print(f'Список один до изменения была - {list_1}')
for i in range(0, len(list_1)):
    list_1[i] += 7.2

print(list_1)
print("//////////////////")
# ###################
pol = input("Вводите число или символ для заполнения списка: ")
li = pol.split(" ")
list_res = []

for i in range(len(li)):
    if li[i].isdigit() and li[i] == '5':
        print(f'пользователь вводил число - 5')

print(f'Список один до изменения была - {li}')
for x in li:
    list_res.append(x)
    list_res.append(x)

li = list_res
print(f'Список После изменений   - {li}')
li.insert(3, list_res[1] + list_res[1])
print(f'Список После добавления символа в индекс 3 - {li}')

print("//////////////////")
# ###################
X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

Y = [[5, 8, 1], [6, 7, 3],  [4, 5, 9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    for j in range(len(X[i])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

print("//////////////////")
# ###################