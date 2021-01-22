# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

data_list = [7, 5, 3, 3, 2]
i = 0
while i < 1:
   element = input('Введите натуральное число, для окончания ввода посто нажмите "Enter": ')
   try:
       element = int(element)
       if (element > 0):
           data_list.append(element)
           data_list.sort()
           data_list.reverse()
           print(data_list)
       elif (element <= 0):
           print('Число должно быть больше 0')
   except ValueError:
       if (element != ''):
           print('Необходимо ввести целое число больше 0')
       else:
           break
print(data_list)