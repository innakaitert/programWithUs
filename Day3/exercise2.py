import codecs

def cleanWord(word):
	new_word = ""
	for letter in word:
		if letter.isalpha():
			new_word = new_word + letter

	return new_word

def mostCommonWords(filename, n):
	common_words = {}

	#Read each line of the text file and and insert each word into the common words dictionary. 
	#if the word already is in the dictionary increase the value by 1
	with codecs.open(filename, "r" ,"ISO-8859-1") as txt:
		for line in txt.readlines():
			temp_list = line.split(" ")
			for word in temp_list:
				clean_word = cleanWord(word)

				print(clean_word)
				if clean_word != "":
					if common_words.get(clean_word) == None:
						common_words[clean_word] = 1
					else:
						common_words[clean_word] += 1


	#starting sort
	most_common = []

	for word in common_words:
		#If the most_common is not full we need to insert into it
		if len(most_common) < n:
			#If most common is empty add the current word to the end
			if len(most_common) == 0:
				most_common.append(word)
			#Run through most common until either we fnd a word in most common with a value less than out word.
			else:
				for x in range( len(most_common) ):
					#If word is greater than the current word in most common insert word before the current word in most common
					if common_words[word] > common_words[ most_common[x] ]:
						most_common.insert(x, word)
						break
					#If we reach the end of the loop without finding a word with a less value than word insert word at the end of the list
					elif x == len(most_common)-1:
						most_common.append(word)
		#If the list is full only add to the list if a word is greater than another word's value and remove one word from the end of the list
		else:
			for x in range( len(most_common) ):
				if common_words[word] > common_words[ most_common[x] ]:
					most_common.insert(x, word)
					most_common.pop()
					break

	#Print each item in the list and its value
	for word in most_common:
		print(word +", "+ str(common_words[word]) )

	# print(most_common)


mostCommonWords("article.txt", 50)
# Add Comment Collapse



