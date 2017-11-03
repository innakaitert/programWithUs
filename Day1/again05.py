side1 = input("What is the lenght of the first side of the triangle?: ")

side2 = input("What is the lenght of the second side of the triangle?: ")

side3 = input("What is the lenght of the third side of the triangle?: ")

if side1 == side2 ==side3:
	print("It is an equilateral triangle.")

elif side1 != side2 != side3:
	print("It is a scalene triangle.")

else:
	print("It is an isosceles triangle.")
