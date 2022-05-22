# написать функцию num_translate(), переводящую числительные от 0 до 10
# с английского на русский язык, доработать функциюб созданную в задании №1
# реализовать корректную работу с числительными, начинающимися с заглавной буквы-
# результат тоже должен быть с заглавной буквы

tr_dict = {"zero": "ноль", "one": "один", "two": "два", "tree": "три",
           "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь",
           "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate(word):
    if word.istitle():
        return str(tr_dict.get(word.lower())).title()
    return tr_dict.get(word)


print(num_translate(input("Enter a word number from 0 to 10: ")))
