class CreditCard:
	card_number = ""
	card_type = ""
	valid = True
	
	def __init__(self, card_number):
		self.card_number = card_number
		

	def getCardNumber(self):
		return self.card_number

	def getCardType(self):
		return self.card_type
		
	def getValid(self):
		return self.valid

	def setCardNumber(self, card_number):
		self.card_number = card_number

	
	def determineCardType(self):
		# We created the string and took indexes from 0 to 2 bc we only need to check
		# first and second numbers for the type
		x = str( self.card_number )[0:2]
		#  all numbers we put in "" bc python doesn't read int
		#  for visa and Discover we add all of te posibilities
		if x in ["40", "41","42","43", "44","45","46", "47","48","49"]:
			print("card_type is Visa")

		elif x == "51" and x == "52" and x =='53' and x== '54' and x == '55':
			print(" Card type is Mastercard")

		elif x == '34' and x == '37':
			print(" Card type is AMEX")

		elif x in ["60", "61","62","63", "64","65","66", "67","68","69"]:
			print("Card type is Discover")
		else:
			print("Card is invalid")
	
		return self.card_type


	def checkLenght(self):

		if len(str(self.card_number)) != 15 or len(str(self.card_number)) != 16:

			print("Invalid card number")
		else:
			print("Card is valid")

		return self.card_number


	def validate(self):

		a = []

		#  we created the empty list a = [] and to put data into it we make for loop
		#  data from card_number goes to the list a = []
		for number in str(self.card_number):
			a.append(number)

		# print(a) - use if need to test the piece

		a1 = a[-2::-2]
		a2 = a[-1::-2]

		# print(a1, a2) - use if need to test the piece

		sum_of_card = 0

		double_a1 = []

		for number in a1:
			double_a1.append(int(number) * 2)
		a1 = double_a1

		for i in a2:
			sum_of_card += int(i)

		for i in a1:
			if i >= 10:
				sum_of_card += 1 + (i-10)
			else:
				sum_of_card += i

		if sum_of_card % 10 == 0:
			return True
		else:
			return False
			# If the code is divisible by 10, returns True, else, it returns False.

		return self.valid
	