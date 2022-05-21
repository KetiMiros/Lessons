# Задача №2 и №3
# Необходимо обработать — обособить каждое целое число кавычками,
# добавить кавычку до и кавычку после элемента списка, являющегося числом,
# и дополнить нулём до двух целочисленных разрядов
# Сформировать из обработанного списка строку

wrong_phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
correct_phrase = []
for i in wrong_phrase:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            correct_phrase.append(f"'{int(0):02}'")
        else:
            correct_phrase.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        correct_phrase.append(i)

# print(correct_phrase)
print(" ".join(correct_phrase))
# --------------------------------------------------------------------------------------------------------
wrong_phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(wrong_phrase):
    if v.isdigit():
        wrong_phrase[i] = f"'{int(v):02}'"
    elif v[1:].isdigit():
        wrong_phrase[i] = f"'{v[0]}{int(v[1:]):02}'"

print(wrong_phrase)
print(" ".join(wrong_phrase))




