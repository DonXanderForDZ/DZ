"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word):
    let = ''
    res_word = ''
    i = 0
    while i < len(word):
        if i == 0:
            let = word[0]
            res_word = res_word + let.upper()
            i += 1
        else:
            res_word = res_word + word[i]
            i += 1
    return res_word

res_str =''
inp_srt = input('Введите строку из слов:\n')
str_list = inp_srt.split()
for n in str_list:
    word1 = int_func(n)
    res_str = res_str + (f'{word1} ')
print(res_str)

