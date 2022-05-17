# Реализовать вывод информации о промежутке
# времени в зависимости от его продолжительности
# в секундах

duration = int(input('Введите время в секундах: '))
days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

print('days:', days, 'hours:', hours, 'minutes:', minutes, 'seconds:', seconds)

# вариант 2
duration = int(input('Введите время в секундах: '))
process = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]

print(process[0], 'days', process[1], 'hours', process[2], 'minutes', process[3], 'seconds')

