name = input("What is your name? ")

age = int(input("Enter you age: "))

age = age + 5

if age > 50:
	print("Hello ",  name,  "You are old!")
elif age <=10:
	print("Hello", name,  " are you old enough to be using this?")
else:
	print("Hello ", name, " You are ", str(age),  " years old.")
