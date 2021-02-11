# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
data_list = []
i = 0
while i < 1:
    element = input('Введите элемент списка, для окончания ввода посто нажмите "Enter": ')
    if element != '':
        data_list.append(element)
    else:
        break
print(data_list)
while i < (len(data_list)-1):
    if (i % 2) == 0:
        k = data_list[i]
        data_list[i] = data_list[i + 1]
        data_list[i + 1] = k
        i += 1
    else:
        i += 1
print(data_list)