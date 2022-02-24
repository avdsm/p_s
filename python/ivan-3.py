# Множества
# numbers = set([1, 1, 2, 4, 2])
numbers = {1, 1, 2, 4, 2, 25, 14, 33}
print(f"{numbers} - {type(numbers)}")
numbers.add(58)
print(numbers)

numbers.discard(25) # Не выводит ошибку если нет опонента
print(numbers)
numbers.pop() # Удаляет 1-й элемент
print(numbers)
numbers.clear() # Удаляет все элементы
print(numbers)