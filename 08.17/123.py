VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
punctMarks = (',', '.', '!', '?', ':', ';')

while True:
	text = input("Введите слово: ")
	word_list = text.split()
	pig_list = []
	if text == "":
		break
	for word in word_list:
		if word[-1] in punctMarks:
			new_word = word[:-1]
		else:
			new_word = word
		pig_list.append(new_word)
	i = 0
	m = 0
	for word in pig_list:
		for letter in word:
			if word[0] in VOWELS:
				pig_word = word + "way"
				pig_list[i] = pig_word.capitalize() if word[0].isupper() else pig_word.lower()
			else:
				for letter in word:
					if letter in VOWELS:
						pig_word = word[word.index(letter):] + word[:word.index(letter)] + "ay"
						pig_list[i] = pig_word.capitalize() if word[0].isupper() else pig_word.lower()
						break
		i += 1
	for item in word_list:
		if item[-1] in punctMarks:
			pig_list[m] = pig_list[m] + item[-1:]
		m += 1

	print(word_list)
	print(pig_list)

