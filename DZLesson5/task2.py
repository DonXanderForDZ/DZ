"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

fp = open("task1.txt", "r", encoding="utf-8")
text_l = fp.readlines()
text_l1 = [el for el in text_l if el != '\n']
text_l2 = [el.replace('\n', '') for el in text_l1]
text_len = len(text_l2)
lists_list = [el.split() for el in text_l2]
word_num = {len(el): el for el in lists_list}
print(f'Всего {text_len} строк')
print('В каждой строке слов:')
for i in word_num:
    print(i)
fp.close()
