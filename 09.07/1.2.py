import random
from math import *

letters = {'a', 'b', 'c'}
str_letters = ''
for i in letters:
    str_letters += str(i)


def all_perms(elements):
    """Генерирует перестановки для переданного множества элементов."""
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


generator_perm = all_perms(str_letters)
print(*list(sorted(generator_perm)))
