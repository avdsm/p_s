s = [45, 35, 61, 70, 15, 44, 33, 85, 59, 60]
j = []
for i in range(len(s)):
    if s[i] >= 60:
        j.append(s[i])

print(f'Результат "{len(j)}" тип {j}')

x = 124568
k = list(str(x))
aa = ''.join(k)
print(k)
print(f'Результат "{aa}" тип {type(aa)}')
# ##################
x = int(input('Выводите число: '))
jj = 0
for i in range(x+1):
    print(" ".join('*' * i))
    jj += 1
    if i == x:
        for j in range(x):
            print(" ".join('*' * (x - j - 1)))

print('Задания выполнена')
