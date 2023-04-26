from typing import SupportsFloat

result = {}

NumSeqType = list[SupportsFloat] | tuple[SupportsFloat, ...] | str


def math(string: NumSeqType) -> dict[str, float]:
    """Функция принимает на вход один аргумент: list, tuple или str, содержащий только целые или вещественные числа. Функция возвращает отсортированный словарь для среднего арифметического, геометрического, квадратичного и гармонического значения аргументов."""

    if not isinstance(string, (str, list, tuple)):
        raise TypeError('сообщение об ошибке типа')

    try:

        if type(string) is str:
            res = []
            for item in string.rstrip().split():
                item = float(item)
                res.append(item)
                string = res
    except ValueError:
        return None

    l = len(string)
    arith = 0
    geom = 1
    quad = 0
    harm = 0

    for num in string:

        if not isinstance(num, SupportsFloat):

            raise TypeError('сообщение об ошибке типа')
        else:

            arith += num
            geom *= num
            quad += num * num
            harm += 1 / num

    result['arithmetic'] = arith / l
    result['geometric'] = pow(geom, 1 / l)
    result['quadratic'] = pow(quad / l, 1 / 2)
    result['harmonic'] = l / harm

    sorted_result = sorted(result.items(), key=lambda i: i[1])
    sorted_result = dict(sorted_result)

    return sorted_result


print(math('1 2 3 4 5'))
print(math((1, 2, 3)))
print(math([1, 2, 3, 4, 5.9]))
