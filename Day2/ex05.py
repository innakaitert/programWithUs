number = int(input ("Enter a number: "))
#  Dictionary 
number_to_roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

# keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9,5,4,1]

roman = ""

#  run untill all numbrs have been converted into the roman numerals
while number > 0:
    #  need to check what the laggest roman numeral that fits into our current numeral
    for divisor in keys:
        # if the number diveded b ythe divisor is not equal to the original number han we know divisor is the largest roman
        if number % divisor != number:
            roman = roman + number_to_roman[divisor]
            number = number - divisor
            break

 print(roman)