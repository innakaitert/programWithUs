import codecs

# function remove non alhabelic characters from the list

def cleanWord(word):
	new_word =""
	for letter in word:
		if letter.isalpha():
			new_word = new_word + letter
	return new_word

common_words = {}

with codecs.open("article.txt", "r", "ISO-8859-1") as txt:
	for line in txt.readlines():
		# split into seperate words
		temp_list = line.split(" ") 
		#  go thoug list one word at the time
		for word in temp_list:
			# remove non alhabelic characters from the list
			clean_word = cleanWord[word]
			print[clean_word]

			if common_words.get(word) == None:
				common_words[words] = 1
			else:
				common_words[words] += 1

#  первірити записи у зошиті до most common word
most_common = []
n = 5

for word in common_words:
	if len()
print(common_words)

		


