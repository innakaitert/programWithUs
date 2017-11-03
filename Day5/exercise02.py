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

	def checkLenght(self):

		#  To check if card has 15 or 16 number we use "if" and the length of the card
		  # Never forget that if you take value from the class add "self"
		  #  str(self.card_number)
		if len(str(self.card_number)) == 15 or len(str(self.card_number)) == 16:

			print("Card is valid")
		else:
			print("Card is not valid")

credit_card1 = CreditCard(4485040993287616)
print(credit_card1.checkLenght())

# it is a piace of the program, in order to put it back to the program
#  last to line must be erased and return self.card_number