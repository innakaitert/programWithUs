#  create the empty dictionary to check for the letters
frequncy = {}


with open ("letters.txt") as txt:
 
	for line in txt.readlines():
		
		for i in xrange(100):
			key = i% 10
			
			if key in d:
				
				d[key]+=1
				
			else:
				d[key] = 1

ptint(d)
# for i in xrange(100): from the site to check if given key already exists in the dictionary 
    # key = i % 10
    # if key in d:
    #     d[key] += 1
    # else:
    #     d[key] = 1