def numberOfVowels(sentence):
	vowels = "aeiou"
	count = 0
	for letter in sentence:
		if letter in vowels:
			count = count + 1
	return count

