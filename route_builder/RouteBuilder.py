'''
Чеклин Павел tscheklin@gmail.com
Проект команды Glina Mess

Класс RouteBuilder 
Предназначен для построения маршрута шашки и создания списка команд для ее перемещения
Вид команды: 
x кол-во шагов y кол-во шагов
Команда оканчивается переходом на новую строку ('\n')
Под количеством шагов подразумевается количество шагов двигателя, эта величиана должна быть 
подобрана опытным путем

Если конечная координта x равна -1 и конечная y равна 0, то
Выход будет производиться за левую часть доски, а если наоборот
(x = 0, y = -1), то за правую

ВИД ПЕРЕМЕННЫХ ДЛЯ ПЕРЕДАЧИ В КЛАСС
x, y - числа от 1 до 8 (поле для шашек)
ИЛИ
x = 1, y = 0 ИЛИ x = 0, y = 1 (проверка идет по y) - ТОЛЬКО ДЛЯ КОНЕЧНЫХ

'''

# ********** ОБЪЯВЛЕНИЕ КОНСТАНТ

# Количетсво шагов двигателя для пермещения шашки на одну клетку по оси X
X_STEPS = 100

# Количество шагов двигателя для пермещения шашки на одну клетку по оси Y
Y_STEPS = 100


class RouteBuilder:
    def __init__(self):
        # Начальные координаты шашки
        self.x1 = 0
        self.y1 = 0

        # Конечные координты шашки
        self.x2 = 0
        self.y2 = 0

        # маршрут (массив команд)
        self.route_list = []

    # Задание координат
    def _set_coordinates(self, start_x, start_y, end_x, end_y):
        self.x1 = start_x
        self.y1 = start_y

        self.x2 = end_x
        self.y2 = end_y

    # проверка на перемещение по диагонали
    def _is_simple(self):
        return abs(self.x1 - self.x2) == abs(
            self.x1 - self.x2) and self.x2 * self.y2 != 0

    # составление команды перемещения
    @staticmethod
    def make_command(start_x, start_y, end_x, end_y):
        return "x %d y %d\n" % ((end_x - start_x) * X_STEPS,
                                (end_y - start_y) * Y_STEPS)

    def complex_root(self):
        # перемещение шашки на место между клеток
        self.route_list.append(self.make_command(
            self.x1, self.y1, self.x1, self.y1 + 0.5 - 1 * (self.y1 > 4)))
        self.y1 = self.y1 + 0.5 - 1 * (self.y1 > 4)

        # перемещение шашки за поле
        self.route_list.append(self.make_command(
            self.x1, self.y1, -2 + 10 * self.y2, self.y1))
        self.x1 = -2 + 10 * self.y2

    # функция построения маршрута (основная функция класса)
    def build_root(self, start_x, start_y, end_x, end_y):
        # задание начальный значений
        self.route_list = []
        self._set_coordinates(start_x, start_y, end_x, end_y)

        # установка магнита на начальное положение шашек
        self.route_list.append(self.make_command(
            1, 1, start_x, start_y))
        self.route_list.append("m\n")

        if self._is_simple():
            self.route_list.append(
                self.make_command(self.x1, self.y1, self.x2, self.y2))
            self.x1, self.y1 = self.x2, self.y2
        else:
            self.complex_root()
        # возврат магнита
        self.route_list.append("o\n")
        self.route_list.append(
            self.make_command(self.x1, self.y1, 1, 1))

        return self.route_list
