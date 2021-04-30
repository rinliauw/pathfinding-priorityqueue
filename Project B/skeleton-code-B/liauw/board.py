from token import Token

class Board:

	#class attribute
	axial_movement = [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]

	#class contructor
	def __init__(self):
		self.upper_tokens = []
		self.lower_tokens = []
		self.block_tokens = []
		self.turn = 1

	#add a token to the board
	def add_token_upper(self, token):
		self.upper_tokens.append(token)

	#add a token to the board
	def add_token_lower(self, token):
		self.lower_tokens.append(token)	

	#add a token to the board
	def add_token_block(self, token):
		self.block_tokens.append(token)

