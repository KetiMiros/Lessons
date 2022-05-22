# реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из 3-х случайных слов, взятых из 3-х
# списков (по одному из каждого)

# return: список случайных шуток
# repeat: уникальные или нет
# n: количество шуток

from random import choice, randrange

nouns = [" авто", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]


def some_jokes(n, repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
        return list_of_j

print(some_jokes(10, True))
