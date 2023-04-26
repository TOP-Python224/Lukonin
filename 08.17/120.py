items = []
result = ''

line = input("Введите слово: ")
while line != "":
	items.append(line)
	line = input("Введите слово: ")

if len(items) == 0:
	print('<пусто>')
elif len(items) == 1:
	print(str(items[0]))
else:

	for i in range(0, len(items) - 2):
		result = result + str(items[i]).join(", ")

	result = result + str(items[len(items)-2]) + " и "
	result = result + str(items[len(items)-1])

	print(result)
