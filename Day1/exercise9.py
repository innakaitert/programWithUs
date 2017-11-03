number = int(input("Enter a number in range 1 -100 to check if it is prime: "))

a=2
for i in range(a, number):
	if (number % i) == 0:
		print(number,  'is not prime')
		break
else:
	print(number,"is a prime number")
	
 
