string = input("Введите текст: \n")

signs = ['.', ',', ':', ';', '!', '?']

words = string.split()

for i, word in enumerate(words):
	if word[-1] in signs:
		words[i] = word[:-1]
		word = words[i]
print(words)
