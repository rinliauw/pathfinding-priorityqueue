from token import Token

class Board:
	#class contructor
	def __init__(self, team):
		self.team = team
		self.our_token = []
		self.enemy_token = []
		self.our_throws = 9
		self.enemy_throws = 9

	#add a token to the board
	def add_token(self, token, player):
		if player == 1:
			self.our_tokens.append(token)
		else:
			self.enemy_tokens.append(token)

	# update token's position in board
	def update_token(self, action, player):
		if player == 1:
			for token in self.our_tokens:
				if token.position == action[1]:
					token.position = action[2]
				break
		else:
			for token in self.enemy_tokens:
				if token.position == action[1]:
					token.position = action[2]
				break