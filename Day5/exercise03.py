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


def validate(self):

		a = []

		#  we created the empty list a = [] and to put data into it we make for loop
		#  data from card_number goes to the list a = []
		for number in str(self.card_number):
			a.append(number)

		print(a)

		a1 = a[-2::-2]
		a2 = a[-1::-2]

		print(a1, a2)

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

credit_card1 = CreditCard(4485040993287616)
print(credit_card1.validate())

#  it is a pieace to test , in order to put back to the program
#  2 last line must be erased and put return self.valid