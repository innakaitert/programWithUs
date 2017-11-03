small_bottles = int(input("How many small bottle did you buy?: "))

big_bottles = int(input("How many big bottles did you buy?: "))

small_bottles_refund = small_bottles * 0.10

big_bottles_refund = big_bottles * 0.25

print("For your small bottles you can return $" + str(small_bottles_refund))

print("For your bigl bottles you can return $" + str(big_bottles_refund))