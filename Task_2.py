# Урок № 1 задание № 2
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7

# создаем пустые спискиб чтобы было куда добавлять
list_cubes = []
add_cubes = []
all_sum = []
i = 0

# возводим в степень при добавлении в список
for i in range(1, 1000, 2):
    list_cubes.append(i ** 3)
    # print(list_cubes)

for ind, var in enumerate(list_cubes):
    sum_1 = 0
    while var > 0:
        sum_1 += var % 10
        var //= 10
    sum_1 % 7 == 0
    all_sum = list_cubes[var]



for j in list_cubes:
    add_cubes.append(j + 17)

all_sum = 0
for ind, var in enumerate(list_cubes):
    sum_1 = 0
    while var > 0:
        sum_1 += var % 10
        var //= 10
        if sum_1 % 7 == 0:
            all_sum += add_cubes[ind]
        list_cubes[ind] += 17

print(all_sum)





