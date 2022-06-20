# Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__)
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.




class Cell:
    def __init__(self, nums):
        self.nums = nums                

    def make_order(self, rows):         
        return '\n'.join(['🌍' * rows for _ in range(self.nums // rows)]) + '\n' + '🌍' * (self.nums % rows)

    def __add__(self, other):
        print("Summ of cell is: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Subtraction of cell is: ")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше, чем во второй, вычитание невозможно!"

    def __mul__(self, other):
        print("Multiply of cell is: ")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Truediv of cell is: ")
        return Cell(self.nums // other.nums)


cell_1 = Cell(12)
cell_2 = Cell(17)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(5))
