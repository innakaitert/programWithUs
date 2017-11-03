
raw_data = []

with open("traffic.txt") as txt:
	for line in txt.readlines():
		# This splits the string line on any spaces it finds and turns it into a list which is then appened to the end of raw_data
		raw_data.append( line[:-1].split(" ") )

room_numbers = []

#Get all of the unique room numbers from raw_data
for item in raw_data:
	#If room number is not in room_numbers append it to the the list as in integer to sort
	if int(item[1]) not in room_numbers:
		room_numbers.append( int(item[1]) )

#Sort the list
room_numbers.sort()

#COnvert integers back into strings
for index in range(len(room_numbers)):
	room_numbers[index] = str( room_numbers[index] )

#Key will be the room number and value will be a list of lists and each list will hold an entery or exit from a room
room = {}

#For each room find all items in raw data and add them to room with a key of the room number
for number in room_numbers:
	#Temp list will hold all items of a particular room
	#At the start of the for loop the list will be reset to an empty list
	temp_list = []
	#Check each item in raw data to see if it matches the current room
	for item in raw_data:
		if item[1] == number:
			#If it does match add it to the list
			temp_list.append(item)
	#Once all items have been checked add the temp list to the dictionary with the key of the room numbers
	room[number] = temp_list

room_times = {}

#For each room get the total time each person spent in that room and add them together
for specific_room in room_numbers:
	#Time_in_room tracks the total time everyone spent in that room
	time_in_room = 0
	#For each person in that room ff this entry is an In to the room find its pair.
	for item in room[specific_room]:
		if item[2] =="I":
			#Search for the pair
			for pair in room[specific_room]:
				#If it is a pair find the different in the enter and exit time for thetime spent in the room 
				if item[0] == pair[0] and pair[2] == "O":
					enter_time = int(item[3])
					exit_time = int(pair[3])
					time_in_room += exit_time-enter_time
					break
	#Insert time into dictionary with the key of the current room number
	room_times[specific_room] = time_in_room


room_people = {}

#This for loop will get all of the unique people in a room
for specific_room in room_numbers:
	#People_in_room will store everyone in a specific room
	people_in_room = []
	#If a person is not in people_in_room we will add them to people_in_room
	for item in room[specific_room]:
		if item[0] not in people_in_room:
			people_in_room.append(item[0])
	#Add people_in_room to room_people iwht the key of the current room
	room_people[specific_room] = people_in_room





#OUTPUT

for specific_room in room_numbers:
	total_people = len(room_people[specific_room])
	time_in_room = room_times[specific_room]
	average_time = time_in_room // total_people
	print("Room "+specific_room+", "+ str(average_time)+
		" minute average visit, "+ str(total_people)+" visitor(s) total")

# Program is desined by Matt