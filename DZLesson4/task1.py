"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

def zp (hours, bid, bonus):
    zp_value = hours*bid + bonus
    return zp_value

if len(argv) != 4:
    print('Запустите программу с параметрами в конфигурации. Например:')
    print(f'{argv(0)} 40 1000 5000')

try:
    hours = float(argv[1])
except ValueError:
    print('Время должно быть числом с плавающей запятой')
    exit(1)
try:
    bid = float(argv[2])
except ValueError:
    print('Ставка почасовой оплаты должна быть числом с плавающей запятой')
    exit(2)
try:
    bonus = float(argv[3])
except ValueError:
    print('Премия должна быть числом с плавающей запятой')
    exit(3)
print(zp(hours, bid, bonus))
