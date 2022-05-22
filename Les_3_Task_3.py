# написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котрором ключи - первые буквы имен, а значения - списки,
# содержащие имена, начинающиеся с соотвествующей буквы

# --------------------------------------вариант 1-------------------------------------------

def thesaurus(*args):
    name_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in name_dict:
            name_dict[letter] += [i]
        else:
            name_dict[letter] = [i]


    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Лапочка"))

# -------------------------------------вариант 2--------------------------------------------

def thesaurus(*args):
    main_list = {}
    for i in sorted(args):
        if i[0] not in main_list:
            main_list[i[0]] = list(filter(lambda element: element.startswith(i[:1]), args))
        print(main_list)


thesaurus("Яна", "Иван", "Мария", "Наташа", "Алексей", "Илья", "Андрей")

