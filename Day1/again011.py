

string = input('Enter a string: ')

if string == "".join(reversed(string)):
	print('It is a palindrome')
else:
	print('It is not a palindrome')

