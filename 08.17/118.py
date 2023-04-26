s = input("Введите строку:\n")
signs = ['.', ',', ':', ';', '!', '?']
words = s.lower().split()

i = 0
for word in words:
	if word[-1] in signs:
		words[i] = word[:-1]
		word = words[i]
	i += 1

l = len(words)

for i in range(l//2):
	if words[i] != words[-1-i]:
		print("Не палиндром")
		break
else:
	print("Палиндром")


