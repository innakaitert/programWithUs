#Import sqlite3 library
import sqlite3

#define CREATE TABLE function. Run this function ONCE.
def createTable():
	connection = sqlite3.connect("movie.db")

	cursor = connection.cursor()

	cursor.execute( '''CREATE TABLE movie(
		id INTEGER PRIMARY KEY,
		title VARCHAR(256),
		director VARCHAR(256),
		lead_actor VARCHAR(256)
		)
		''' )

	connection.commit()

	connection.close()

#Open connection to database
connection = sqlite3.connect("movie.db")

#Create cursor to interact with database
cursor = connection.cursor()

title = "Star Wars"

director = "George Lucas"

lead_actor = "Mark Hamill"

#Execute SQLITE3 Statements and use a ? in place of any variables. Put variables in a tuple after the statement in the same order as the ?s
cursor.execute('''INSERT INTO movie(title,director,lead_actor) VALUES (?,?,?) ''', (title, director, lead_actor) )

#Save your changes to the database
connection.commit()

#Close connection to database
connection.close()
