"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

fp = open("task1.txt", "w", encoding="utf-8")
i = 0
while i != '':
    i = input('Введите строку: ')
    st = i + '\n'
    fp.write(st)
fp.close()