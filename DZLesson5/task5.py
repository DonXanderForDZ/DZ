"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
from functools import reduce

fp = open("task5.txt", "w", encoding="utf-8")
for i in range(100):
    n = random.randint(1, 100)
    fp.write(f'{n} ')
fp.close()
fp = open("task5.txt", "r", encoding="utf-8")
text_l = fp.readline()
text_l1 = text_l.split()
text_l2 = [int(el) for el in text_l1]
el_sum = reduce(lambda acc, x: acc+x, text_l2)
print(f'Сумма элементов файла равна: {el_sum}')
