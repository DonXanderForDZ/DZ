# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

data_list = [None, 77, 7.7, bin(77), complex(5, 7), 'bums', list('data'), tuple('1234567890'),
             set('буквы'), dict(key_1='val_1', key_2='val_2'), bool(5)]
for i in data_list:
    if type(i) is type(None):
        print('Тип элемента: NoneType')
    elif type(i) == int:
        print('Тип элемента: целое число')
    elif type(i) == float:
        print('Тип элемента: число с плавающей запятой')
    elif type(i) == bin:
        print('Тип элемента: двоичное число')
    elif type(i) == complex:
        print('Тип элемента: комплексное число')
    elif type(i) == str:
        print('Тип элемента: строка')
    elif type(i) == list:
        print('Тип элемента: список')
    elif type(i) == tuple:
        print('Тип элемента: кортеж')
    elif type(i) == set:
        print('Тип элемента: множество')
    elif type(i) == dict:
        print('Тип элемента: словарь')
    elif type(i) == bool:
        print('Тип элемента: булево выражение')

