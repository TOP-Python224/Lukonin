s1 = input("Введите первое слово: ")
s2 = input("Введите второе слово: ")

result1 = {}
result2 = {}

for i in s1:
    if i in result1:
        result1[i] += 1
    else:
        result1[i] = 1

for i in s2:
    if i in result2:
        result2[i] += 1
    else:
        result2[i] = 1

if result1 == result2:
    print("Введенные слова являются анаграммами! ")
else:
    print("Введенные слова не являются анаграммами! ")

