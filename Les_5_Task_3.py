# реализовать генератор, возвращающий кортежи вида (<tutor>, <klass)
# количество генерируемых кортежей быть больше длины списка tutors
# если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None)
# доказать, что создан генератор, проверить ратоту до истощения


import itertools
from itertools import islice, zip_longest

tutors = ["Иван", "Анастасия", "Пётр", "Сергей", "Дмитрий", "Борис", "Елена", "Кирилл"]
klasses = ['9A', '7B', '9Б', '9В', '8Б', '10А']

rezult = (i for i in itertools.zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(rezult))
print(*islice(rezult, 9))
print((list(islice(rezult, 3))))

# ------------------------------------------- вариант2 ------------------------------------------------


tutors = ["Иван", "Анастасия", "Пётр", "Сергей", "Дмитрий", "Борис", "Елена", "Кирилл"]
klasses = ['9A', '7B', '9Б', '9В', '8Б', '10А']
#
together = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))
#
print(type(together), *together, sep='\n')

# print(next(together))                 # проверка работы до истощения, дальше некуда идти
