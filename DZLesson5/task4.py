"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
fp = open("task4.txt", "r", encoding="utf-8")
text_l = fp.readlines()
text_l1 = [el for el in text_l if el != '\n']
text_l2 = [el.replace('\n', '') for el in text_l1]
lists_list = [el.split() for el in text_l2]
rem_list = [['Один', '—', '1'], ['Два', '—', '2'], ['Три', '—', '3'], ['Четыре', '—', '4']]
res_list = []
for i in lists_list:
    for n in rem_list:
        if i[2] == n[2]:
            i = n
            res_list.append(i)
fp2 = open("task4_2.txt", "w", encoding="utf-8")
for i in res_list:
    fp2.write(f'{i[0]} {i[1]} {i[2]}\n')
fp.close()
fp2.close()