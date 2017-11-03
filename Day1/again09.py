number = int(input("Enter a number in range 1 -100 to check if it is prime: "))

# start with 2 bc 0 and 1 are prime numbers, we don't nedd to check them

for dividing_number in range(2, number):

	if (number % dividing_number) == 0:
		
		print(number,  'is not prime')
		break
else:
	print(number,"is a prime number")