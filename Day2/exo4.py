def isOdd(number):
	if number%2 ==1:
		#Number is odd
		return True
	else:
		#Number is even
		return False
		
list_of_numbers = [9,3, 4, 5, 12, 35, 45,23, 0,1, 74, 69, 13]

odd_numbers = []

index = 0

while index< len(list_of_numbers):
	if isOdd( list_of_numbers[ index ]):
		odd_numbers.append( list_of_numbers.pop(index))
	else:
		index = index + 1

print(list_of_numbers)
print(odd_numbers)


# for number in list list_of_numbers:
# 	if isOdd(number) == True:
# 		odd_numbers.append(number)

# print(odd_numbers)