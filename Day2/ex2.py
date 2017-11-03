message = str(input("Enter the sentance"))
new_massage = ""
capitalize_next = True

for x in range(len(message)):
	if message[x] =='.'  or message[x] == '!' or message[x] == '?':
		capitalize_next = True
	if capitalize_next == True and message[x].isalpha():
		new_massage += message[x].capitalize()
		capitalize_next = False
	elif message[x] == "i" and message[x-1] == " " and message[x+1] == " ":
		new_massage += message[x].capitalize()
	else:
		new_massage+= message[x]

print(new_massage)
