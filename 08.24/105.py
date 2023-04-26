dict1 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
dict2 = {v: k for k, v in dict1.items()}


def decimal_to_any(num: int, *, new_base: int = 16) -> str:
	"""Функция преобразует десятичное число num в число в системе счисления new_base = 16, по умолчанию."""
	q = num // new_base
	r = num % new_base
	result = str(r)

	while q > 0:
		r = q % new_base
		q = q // new_base
		if r > 9:
			result = str(dict1[r]) + result
		else:
			result = str(r) + result
	return result


def any_to_decimal(num: int, *, base: int = 16) -> int:
	"""Функция преобразует число num в системе счисления base = 16 по умолчанию, в десятичное число."""
	result = 0
	length = len(num)
	for i in range(length):
		if num[i].isalpha():
			result += (dict2[num[i].title()]) * base**(length-1)
		else:
			result += int(num[i]) * base**(length-1)
		length -= 1
	return result


def any_to_any(num: str, base_default: int, new_base_default: int) -> str:
	"""Функция преобразует число num из исходной системы счисления в новую."""
	return decimal_to_any(
		any_to_decimal(
			str(num),
			base=base_default
		),
		new_base=new_base_default
	)


num = input('Введите число в исходной системе счисления: ')
base_default = int(input('Исходная система счисления (2-16): '))
new_base_default = int(input('Введите требуемую систему счисления (2–16): '))

if 2 <= base_default <= 16 and 2 <= new_base_default <= 16:
	print(any_to_any(num, base_default, new_base_default))
else:
	print("Допустимый диапазон систем счисления: от 2 до 16.")
