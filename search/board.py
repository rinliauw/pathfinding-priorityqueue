class Board:

	#class attribute
	tokens = []
	blocked_hex = None
	radius = None
	2d_array = None

	#class contructor
	def __init__(self, radius):
		self.radius = radius

	def create_array():
		
	#set a hex to be blocked
	def set_blocked_hex(position):
		self.blocked_hex.append(position)

	#add a token to the board
	def add_token(token):
		self.tokens.append(token)

	#check if the position is inside the board range
	def inside_board(position):