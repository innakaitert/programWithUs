
class Bucket:
	name = ""
	max_volume = 0
	current_volume = 0

	def __init__(self, name, max_volume, current_volume):

		self.name = name
		self.max_volume = max_volume
		self.current_volume = current_volume

	def getname(self):
			return self.name

	def setname(self, name):
			self.name = name

	def getmax_volume(self):
			return self.max_volume

	def setmax_volume(self, max_volume):
			self.max_volume = max_volume

	def getcurrent_volume(self):
			return self.current_volume

	def setcurrent_volume(self):
			self.current_volume = current_volume

	def transfer(self, volume_transfer):
		self.current_volume = self.current_volume + min(self.max_volume - self.current_volume, volume_transfer )

bucket1 = Bucket("Green", 10, 3)

bucket2 = Bucket("Red", 8, 2)

bucket2.transfer(4)

print(bucket2.getcurrent_volume())
	




