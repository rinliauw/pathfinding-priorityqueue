class Token:

	#class constructor
	def __init__(self, position, category, team):
		self.position = position # (x, y)
		self.category = category # r, p, s
		self.team = team # 'upper' or 'lower'