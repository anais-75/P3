
class Items():
	def __init__(self, name):
		
		self.name = name

	def __repr__(self):
		return self.name
	
	"""I define here a special class which compares me two objects of type Items"""
	def __eq__(self, items):
		return self.name == items

if __name__ == "__main__":  
	print("items")
