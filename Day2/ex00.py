def isOdd(number):
	if number%2 ==1:
		#Number is odd
		return True
	else:
		#Number is even
		return False

word = "civic"

first_half = word[0: len(word)//2]

if isOdd(len(word)):
	second_half = word[-1: (len(word)//2): -1]

else:
	second_half = word[-1: (len(word)//2)-1: -1]

if first_half == second_half:
	print("Palindrome")
else:
	print("Not a Palindrome")


print(first_half)
print(second_half)