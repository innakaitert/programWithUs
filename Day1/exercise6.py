# base_size = int(input("How many stars should be in the patten? "))

# for row in range (base_size):
# 	for col in range( row + 1):
# 		print('*', end='')
# 	print()

# for row in range (0, base_size):
# 	for col in range (base_size, row, -1):
# 		print('*', end='')
# 	print()

stars = int(input("How tall is the piramid: "))

for x in range (1, stars * 2):
	if x <= stars:
		for y in range(x):
			print('*', end = ' ')
		print()
	else:
		difference = x - stars
		for z in range( stars - difference ):
			print('*', end = " ")

		

