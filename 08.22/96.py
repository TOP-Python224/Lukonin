decimal = '0123456789'
sign = '+-'


def isInteger(s: str) -> bool:
    """Функция принимает на ввод строку, удаляет все пробелы и проверяет является ли введенная строка числом."""
    new_s = ""

    for i in s:
        if i == " ":
            continue
        else:
            new_s += i
    cnt = 0
    for item in new_s:
        if item in decimal or item in sign:
            cnt += 1
        else:
            continue
    l = len(new_s)
    if new_s[0] in sign and cnt == l:
        return True
    if cnt == l:
        return True
    else:
        return False


s = input("Введите строку: ")

if isInteger(s):
    print("Строка является целым числом!")
else:
    print("Строка не является целым числом")

