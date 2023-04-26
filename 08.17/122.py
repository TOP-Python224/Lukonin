VOWELS = ('a', 'e', 'i', 'o', 'u')

word = ""
while True:
	word = input("Введите текст: ")
	word_list = word.lower().split()
	if not word:
		break
	else:
		for word in word_list:
			if word[0] in VOWELS:
				word = word + "way"
				print(word)
			else:
				for letter in word:
					if letter in VOWELS:
						word = word[word.index(letter):] + word[:word.index(letter)] + "ay"
						print(word)
						break
