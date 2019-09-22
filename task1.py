def find_words():
	item=open("words.txt")
	for word in item:
		word=word.strip()
		if len(word)>=20:
			print(word)
    find_words()
