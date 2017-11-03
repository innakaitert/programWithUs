from view import View
from model import CreditCard

my_view = View()

card_num = my_view.takeInput("Enter a card number: ")

my_card = CreditCard(card_num)

#GET CARD TYPE
#_______________________________________________________________________
#dictionary of lists with each list containing all possible starting strings for that card type
card_types = {"Visa":["4"], "MasterCard":["51","52","53","54","55"], "AMEX":["34","37"],"Discover":["6"]}

#For each card type in dictionary get all starting strings and compare them to the card number
for card_name in card_types.keys():
	for starting_number in card_types[card_name]:
		#Gets the first values of the string card_number based on the length of the current starting string
		#Then compares that against the starting string.
		if my_card.getCardNumber()[0:len(starting_number)] == starting_number:
			my_card.setCardType(card_name)
			break

#Create a dictionary with the key of a card type and a value of the length it needs to be
card_lengths = {"Visa":16, "MasterCard":16, "AMEX":15, "Discover":16}

#If the length of card_number is not equal to the length based on the dictonary then the card type is invalid
if card_lengths.get(my_card.getCardType(), -1) != len(my_card.getCardNumber()):
	my_card.setCardType("INVALID")
#_______________________________________________________________________________________
#END OF GET CARD TYPE

#LUHN ALGORITHM
#___________________________________________________________
# Slices the string card_number on every other character and converts to a list
double = list(my_card.getCardNumber()[-2::-2])
single = list(my_card.getCardNumber()[-1::-2])

#Convert each item in double to an integer and double it
for index in range(len(double)):
	double[index] = int(double[index])*2

#Convert every item in single to an integer
for index in range(len(single)):
	single[index] = int(single[index])

card_sum = 0

#Sum double using for loop. If an item in double is greater than 10 add 1 and item-10 instead
for item in double:
	if item >= 10:
		card_sum = card_sum + 1 + (item-10)
	else:
		card_sum = card_sum + item

#Add each item in single to the sum
for item in single:
	card_sum = card_sum + item


# If the sum is divisible by 10 then the card_number is valid.
if card_sum%10 == 0:
	my_card.setValid("VALID")
else:
	my_card.setValid("INVALID")
#__________________________________________________________________
#END LUHN ALGORITHM


print(my_card.getCardType())
print(my_card.getValid())