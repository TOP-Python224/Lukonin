sp = input().split()
result = {}

for i in sp:
	ind = i.find('.')
	text_r = i[ind:]
	text_l = i[:ind]
	if i in result:
		print(f'{text_l}_{result[i]}{text_r}', end=' ')
	else:
		print(i, end=' ')
	result[i] = result.get(i, 1) + 1

	