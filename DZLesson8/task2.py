"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByNull:
    def __init__(self, divider=0, denominator=0):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"На ноль делить нельзя")


div = DivisionByNull()
print(DivisionByNull.divide_by_null(50, 0))
print(DivisionByNull.divide_by_null(50, 0.5))
print(div.divide_by_null(100, 0))