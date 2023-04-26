text = {}

for i in input('Введите текст: ').split():
    i = i.strip('.,!?:;-').lower()
    text[i] = text.get(i, 0) + 1 

print(min(text.items(), key=lambda x: (x[1], x[0]))[0])