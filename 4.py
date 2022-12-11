# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def coefficient_random():
    return random.randint(0, 100)

def create_polynominal(n):
    coefficient_list = []
    for i in range(n+1):
        dop = coefficient_random()
        coefficient_list.append(dop)
    return (coefficient_list)

def create_file(k):
    my_list = create_polynominal(k)

    file = open('polynominal.txt', 'w')

    for num in range(len(my_list)-1):
        file.write (f'{my_list[num]} * x^ {k} + ')
        k = k-1
    file.write(f'{my_list[len(my_list)-1]} ')

    file.close()


k = 2
create_file(k)