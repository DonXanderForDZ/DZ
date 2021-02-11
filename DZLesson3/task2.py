"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""
def in_fun(name, sec_name, year, city, email, phone):
#    user_par = [name, sec_name, year, city, email, phone]
#    print(user_par)
    print (f'{name} {sec_name} {year} {city} {email} {phone}')

in_fun (name = input('Введите имя: '), sec_name = input('Введите фамилию: '),year =
        input('Введите год рождения: '), city = input('Введите город: '),email =
        input('Введите email: '), phone = input('Введите номер телефона: '))
