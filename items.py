# from constants import *

class Items():
	def __init__(self, name):
		
		self.name = name

	def __repr__(self):
		return self.name
	
	"""Je définis ici une classe spéciale qui me compare deux objet de type Items	"""
	def __eq__(self, items):
		return self.name == items

if __name__ == "__main__":
	#test
	print("items")
