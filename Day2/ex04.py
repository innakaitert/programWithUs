# limit = int(input("Enter the limit: "))

# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)

# print(prime_eratosthenes(limit))

limit = int (input(" enter the limit: "))

sieve_list =  list(range(2, limit+1))

# while loop moves from start list to end of list 
# we use a while loop bc we will be removing items from the list
index = 0
while index < len(sieve_list):

# index2 starts at index + 1 bc we want to chekc 
	index2 = index+1
	while index2 < len(sieve_list):
		if sieve_list[index2]%sieve_list[index] == 0:
			sieve_list.pop(index2)
		else:
			index2 = index2 + 1

	index = index + 1

print(sieve_list)