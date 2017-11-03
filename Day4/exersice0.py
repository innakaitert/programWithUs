class Car:
	make = ""
	model = ""
	year = 0
	color = ""
	milage = 0.0

	def __init__(self, make, model, year, color, milage):
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.milage = milage

	def getMake(self):
		return self.make

	def setMake(self, make):
		self.make = make

	def getYear(self):
		return self.year

	def setMilage(self,milage):
		self.milage = milage

	def getMilage(self):
		return self.milage

	def drive(self, miles_driven):
		self.milage = self.milage + miles_driven


my_car = Car("toyota","carolla",2010,"red",50000.0)

my_car2 = Car("jaguar", "XJ", 2017, "Silver", 0.0)

print(my_car.make)

print( my_car.getYear() )

my_car2.setMilage( my_car2.getMilage()+20)

my_car2.drive(20)