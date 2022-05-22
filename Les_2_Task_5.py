# Урок №2 задание № 5
# создать список вручную, содержащий цены на товары
# вывести на экран цены через запятую в одну строку
# цена должна отображаться в виде <r> руб <kk> коп
# вывести цены отсортированне по возрастанию, без нового списка
# создать новый список с теми же ценами, но по убыванию
# вывести цены самых дорогих товаров

prices = [57.02, 45.56, 55, 20.17, 1.76, 51, 98.90, 70.01,
         65, 39, 90.48, 59.11, 88.08, 93, 8.53]

print(f"\n\n{'*' * 55} часть_1 {'*' * 55}\n")
print(f"{'-' * 35} вариант_1\n")

for i in prices:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):02d} коп ,", end=" ")

print(f"\n\n{'-' * 35} вариант_2\n")

for i in prices:
    rub, kop = int(i // 1), int(f"{i % 1:.02f}"[2:])
    print(f"{rub} руб {kop:02d} коп,", end=" ")

print(f"\n\n{'*' * 55} часть_3 {'*' * 55}\n")


print(f"ID base: {id(prices)} - {prices}")
prices.sort()
print(f"ID change: {id(prices)} - {prices}")

print(f"\n\n{'*' * 55} часть_4 и 5 {'*' * 55}\n")


n_list = sorted(prices, reverse=True)
print(f"ID change: {id(n_list)} - {n_list}\n{n_list[:5]}")

print(f"ID change: {id(n_list)} - {n_list}\n{n_list[:5][::-1]}")



