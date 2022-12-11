# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

result = {}

with open('polynominal.txt') as f:
    for line in f:
        line1 = line
    print(line1)

with open('polynominal2.txt') as f:
    for line in f:
        line2 = line
    print(line2)

file = open('polynominal_summa.txt', 'w')

file.write(f'{line1} + {line2} ')

file.close()