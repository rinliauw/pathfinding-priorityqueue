class Token:

	#class constructor
	def __init__(self, position, category, team):
		self.position = position
		self.category = category
		self.team = team
		self.path = []
		self.target = None
		self.viable_target = []
		self.finished = False

	def get_category(self):
		return self.category