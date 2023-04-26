points = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}

word = input('Введите слово: ').upper()

sum = 0

for i in word:
	for key, value in points.items():
		if i in value:
			sum += key

print(sum)