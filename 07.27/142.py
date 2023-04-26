text = input('Введите строку: ')

dict_uniq = {}

for ch in text:
    dict_uniq[ch] = 1

print(f'Строка содержит, {len(dict_uniq)} уникальных символов')
