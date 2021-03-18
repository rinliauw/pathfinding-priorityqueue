class Token:

	#class attributes
	position = None			#current position of the token
	category = None			#category of the token. Either 'r', 'p', or 's'
	team = None				#team of the token. Either 'upper' or 'lower'

	#class constructor
	def __init__(self, position, category, team):
		self.position = position
		self.category = category
		self.team = team

	def get_category():
		return self.category
		