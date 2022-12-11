# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n=int(input("Введите размер массива: "))
lst = []
for i in range(n):
    lst.append(random.randint(1, 10))
print(lst)
lst2 = []
for i in lst:
    if lst.count(i) == 1:
        lst2.append(i)
print(lst2)