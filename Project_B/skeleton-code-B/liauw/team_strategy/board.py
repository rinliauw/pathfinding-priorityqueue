from token import Token

class Board:
	#class contructor
	def __init__(self):
		self.upper_tokens = [] # list of all upper tokens
		self.lower_tokens = [] # list of all lower tokens
		self.turns = 0 # initial turns

	#add a token to the board
	def add_token(self, token, player):
		if player == 'upper':
			self.upper_tokens.append(token)
		else:
			self.lower_tokens.append(token)

	# update token's position in board
	def update_token(self, action, player):
		if player == 'upper':
			for token in self.upper_tokens:
				if token.position == action[1]:
					token.position = action[2]
				break
		elif player == 'lower':
			for token in self.lower_tokens:
				if token.position == action[1]:
					token.position = action[2]
				break

	# checks if the game is finished
	def check_finished(self, action, player):
		if self.turns == 360:
			return True