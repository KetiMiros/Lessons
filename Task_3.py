# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
# экран отдельной строкой для каждого из чисел в интервале от 1 до 100

# user_percent = int(input('Введите число поцентов от 1 до 100: '))

user_percent = []
for user_percent in range(101):
    if user_percent % 10 == 1 and user_percent % 100 != 11:
        print(user_percent, 'процент')
    elif 1 < user_percent % 10 < 5 and not 11 < user_percent % 100 < 5:
        print(user_percent, 'процента')
    else:
        print(user_percent, 'процентов')
# пока не разобралась как сделать вывод 1 раз,а не 100)
