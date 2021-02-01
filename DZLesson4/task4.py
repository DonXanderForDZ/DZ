"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

def com_fun (x):
    pos_list = [el for el in range(0, len(sourse_list)) if sourse_list[el] == x]
    l_pos = len(pos_list)
    return l_pos

sourse_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
sourse_set = {el for el in sourse_list}
b_list = [el for el in sourse_set]
diff_list = [x for x in b_list if com_fun(x) > 1]
res_list = [el for el in sourse_list if el not in diff_list]
print(res_list)