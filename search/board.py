from .token import Token
class Board:

	#class attribute
	axial_movement = [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]

	#class contructor
	def __init__(self):
		self.upper_tokens = []
		self.lower_tokens = []
		self.block_tokens = []

	#add a token to the board
	def add_token_upper(self, token):
		self.upper_tokens.append(token)

	#add a token to the board
	def add_token_lower(self, token):
		self.lower_tokens.append(token)	

	#add a token to the board
	def add_token_block(self, token):
		self.block_tokens.append(token)

	def find_token_paths(self):
		for token in self.upper_tokens:
			token.get_viable_target(self.lower_tokens)
			token.get_nearest_target()
			token.get_token_path(self.block_tokens)