#  create the empty dictionary to check for the letters
frequncy = {}

# відкрити текстовій файл щоб передивитись літери
with open ("letters.txt") as txt:
 # в кожній лінії передивитись на букви
	for line in txt.readlines():
		# луп для перевірки чи повторюються букви
		for letter in line:
			# якщо буква повторюється 
			if letter in frequncy:
				# ми її додаємо
				frequncy[letter]+=1
				# або переходимо до іншої букви
			else:
				frequncy[letter] = 1

print(frequncy)

# for i in xrange(100): from the site to check if given key already exists in the dictionary 
    # key = i % 10
    # if key in d:
    #     d[key] += 1
    # else:
    #     d[key] = 1