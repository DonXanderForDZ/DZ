"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

fp = open("task3.txt", "r", encoding="utf-8")
text_l = fp.readlines()
text_l1 = [el for el in text_l if el != '\n']
text_l2 = [el.replace('\n', '') for el in text_l1]
lists_list = [el.split() for el in text_l2]
zp_dict = {}
for i in lists_list:
    z_dict = {i[0]: i[1]}
    zp_dict.update(z_dict)
mzp_list = [el for el in zp_dict if int(zp_dict.get(el)) < 20000]
n = 0
over = 0
for i in zp_dict:
    over = over + int(zp_dict.get(i))
    n += 1
if n == 0:
    n += 1
over = over / n
print(f'Средняя зарплата: {over}')
print(f'Зарплата менее 20000 у {mzp_list}')
fp.close()
