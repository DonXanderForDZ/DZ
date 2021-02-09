"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

fp = open("task7.txt", "r", encoding="utf-8")
text_l = fp.readlines()
text_l1 = [el for el in text_l if el != '\n']
text_l2 = [el.replace('\n', '') for el in text_l1]
lists_list = [el.split() for el in text_l2]
res_dict = {}
aver = 0
n = 0
for i in lists_list:
    plus_val = int(i[2])
    min_val = int(i[3])
    profit = plus_val - min_val
    if profit >= 0:
        z_dict = {i[0]: profit}
        res_dict.update(z_dict)
        n += 1
        aver += profit
if n == 0:
    n += 1
aver = round(aver / n, 2)
aver_dict = {'average_profit': aver}
res_list = [res_dict, aver_dict]
print(res_list)
with open("task7.json", "w" ) as fp_j:
    json.dump(res_list, fp_j)
