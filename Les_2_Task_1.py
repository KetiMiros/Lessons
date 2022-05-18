# вариант решения № 1

name_1 = 15 * 3
print(type(name_1))  # class 'int'
print(name_1)

name_2 = 15 / 3
print(type(name_2))  # class 'float'
print(name_2)  # 5.0

name_3 = 15 // 2
print(type(name_3))  # class 'int'
print(name_3)  # 7

name_4 = 15 ** 2
print(type(name_4))  # class 'int'
print(name_4)  # 225

# вариант решения №2

list_numbers = [15 * 3, 15 / 3, 15 // 3, 15 ** 2]
for i in list_numbers:
    print(i)
    print(type(i))


