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

credit_card1 = CreditCard(4485040993287616)
print(credit_card1.determineCardType())

# it is a piace of the program, in order to put it back to the program
#  last to line must be erased and return self.card_type