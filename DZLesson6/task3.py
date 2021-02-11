"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name +' ' + self.surname

    def get_total_income(self):
        return self._income.get('оклад') + self._income.get('премия')

clss_el = Position(input('Введите имя сотрудника: '),input('Введите фамилию сотрудника: '),
                   input('Введите должность сотрудника: '), int(input('Введите оклад сотрудника: ')),
                   int(input('Введите премию сотрудника: ')))
print(f'Полное имени сотрудника: {clss_el.get_full_name()}')
print(f'Доход с учетом премии: {clss_el.get_total_income()} руб.')
