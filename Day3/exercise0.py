# read the file
with open ('word. txt') as txt: 
	#  write to the file
with open ('eigthletter.txt', "w") as nex_txt:
	for line in txt.readlines():
		# will read the words that are only 8 letters in the file
		if len(line) >= 8:
			print(line, end='')
			#  write to the file
			nex_txt.write(line)

