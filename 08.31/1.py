import math

from typing import Callable
from numbers import Real


def math_func(func_obj: Callable, *args: Real, total: bool = True) -> str | float:
	"""Принимает на ввод функцию и выводит округленное до 2-х знаков результат в формате str или float"""
	result = func_obj(*args)
	return str(round(result, 2)) if total else float(round(result, 2))


print(math_func(lambda k, x, b: k * x + b, 2, 3, 4))
print(math_func(lambda a, x, b, c: a * x ** 2 + b * x + c, 1.2, 2.3, 3.4, 4.5))
print(math_func(lambda x: math.sin(x), 5.7))
print(math_func(lambda k, x: k / x, 10, 5))
print(type(math_func(lambda k, x: k / x, 10, 5, total=False)))
print(type(math_func(lambda k, x: k / x, 10, 5)))
