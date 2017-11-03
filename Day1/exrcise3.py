small_bottles = int(input("How many bottles that are less than litter "+
	"did you use? "))
big_bottles = int(input("How many bottles that are more than litter "+
	"did you use? "))

refund1 = small_bottles * 0.10

refund2 = big_bottles * 0.25

print("You will recieve $" + str(refund1) + " for the small bottles.")

print("You will recieve $" + str(refund2) + " for the small bottles.")