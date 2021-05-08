from token import Token

class Board:
	#class contructor
	def __init__(self):
		self.my_tokens = [] # list of all upper token
		self.opponent_tokens = [] # list of all lower tokens

		# defines unique team (r,p,s)
		self.defeated_tokens = {'mine': [], 'opponent': []} # move upper/lower's token to defeated -> need to be updated somewhere
		self.throws_count = {'mine': 0, 'opponent': 0} # count of throws
		self.status = {'mine': None, 'opponent': None} # draw, win, lose (according to player 1)
		self.turns = 0 # initial turns -> need to be updated somewhere

	#add a token to the board
	def add_token(self, token, player):
		if (player == 'mine'):
			self.my_tokens.append(token)
		elif (player == 'opponent'):
			self.opponent_tokens.append(token)

	# update token's position in board
	def update_token(self, action, player):
		if (player == 'mine'):
			for token in self.my_tokens:
				if token.position == action[0]: # changes position to latest position
					token.position = action[1]
				break
		elif (player == 'opponent'):
			for token in self.opponent_tokens:
				if token.position == action[0]:
					token.position = action[1]
				break

	# checks if the game is finished
	def check_finished(self):
		if self.turns == 360: # if 360th turn
			self.status['mine'] = 'Draw'
			self.status['opponent'] = 'Draw'
		# if 1 player has throwed 9 times and all the tokens are defeated
		elif ((self.throws_count['mine'] == 9) && (len(self.defeated_tokens['mine']) == 9)):
			self.status['mine'] = 'Lose'
			self.status['opponent'] = 'Win'
		elif ((self.throws_count['opponent'] == 9) && (len(self.defeated_tokens['opponent']) == 9)):
			self.status['mine'] = 'Win'
			self.status['opponent'] = 'Lose'
		# if p1 throwed 9 times n all p1's tokens cant be defeated by p2's tokens 
		else:
			self.update_invincible()

	
	def update_invincible(self):
		if self.throws_count['opponent'] == 9 && check_invincible():
			self.status['mine'] = "Win"
			self.status['opponent'] = 'Lose'
		else if self.throw_counts['mine'] == 9 && (!check_invincible()):
			self.status['mine'] = "Lose"
			self.status['opponent'] = "Win"
		else:
			self.status['mine'] = "Draw"
			self.status['opponent'] = "Draw"
		return

	# check if mine is invincible
	def check_invincible(self):
		for my_token in self.my_tokens:
			for opponent_token in self.opponent_tokens:
				if opponent_token.category is self.is_beatable(opponent_token.category, my_token.category):
					

	def is_beatable(self, opponent_category, my_category):
		if opponent_category == "s" && my_category == "p":
			return True
		elif opponent_category == "p" && my_category == "s":
			return False
		elif opponent_category == "p" && my_category == "r":
			return False