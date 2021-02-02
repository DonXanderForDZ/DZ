"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
#from functools import reduce
fp = open("task6.txt", "r", encoding="utf-8")
text_l = fp.readlines()
text_l1 = [el for el in text_l if el != '\n']
text_l2 = [el.replace('\n', '') for el in text_l1]
lists_list = [el.split() for el in text_l2]
res_dict = {}
for i in lists_list:
    i[0] = i[0].replace(':','')
    m_list = []
    for n in i:
        n = ''.join(x for x in n if x.isdigit())
        if n != '':
            m_list.append(n)
    int_list = [int(el) for el in m_list]
    el_sum = 0
    for k in int_list:
        el_sum += k
#   el_sum = reduce(lambda acc, x: acc+x, int_list)
    z_dict = {i[0]: el_sum}
    res_dict.update(z_dict)
print(res_dict)
fp.close()
