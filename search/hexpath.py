class HexPath:

	def __init__(self, position, next = None): 
		self.parent = None
		self.f_cost = None
		self.g_cost = None
		self.position = position

	def set_f_cost(self, cost):
		self.f_cost = cost

	def set_parent(self, parent):
		self.parent = parent