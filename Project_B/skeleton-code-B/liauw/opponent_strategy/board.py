from token import Token

class Board:
	#class contructor
	def __init__(self):
		self.upper_tokens = [] # list of all upper token
		self.lower_tokens = [] # list of all lower tokens
		self.invincible = {'upper': set(), 'lower': set()}
		self.defeated_tokens = {'upper': [], 'lower': []} # move upper/lower's token to defeated
		self.throws_count = {'upper': 0, 'lower': 0} # count of throws
		self.turns = 0 # initial turns
		self.status = {'upper': None, 'lower': None} # draw, win, lose (according to player 1)
		self.player = None # marks which team am i

	#add a token to the board
	def add_token(self, token, player):
		if player == 'upper':
			self.upper_tokens.append(token)
		else:
			self.lower_tokens.append(token)
		self.player = player

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
	def check_finished(self):
		if self.turns == 360: # if 360th turn
			self.status['upper'] = 'Draw'
			self.status['lower'] = 'Draw'

		# if 1 player has throwed 9 times and all the tokens are defeated
		else if ((self.throws_count['upper'] == 9) && (len(self.defeated_tokens['upper']) == 9)):
			self.status['upper'] = 'Lose'
			self.status['lower'] = 'Win'
		else if ((self.throws_count['lower'] == 9) && (len(self.defeated_tokens['lower']) == 9)):
			self.status['lower'] = 'Win'
			self.status['lower'] = 'Lose'
		# if p1 throwed 9 times n all p1's tokens cant be defeated by p2's tokens 
		else:
			self.check_invincible()


	# checks if any token is defeated, then put it in self.defeated_tokens
	def update_defeated(self):
		
		return
	
	def check_invincible(self):
		if self.throws_count['lower'] == 9 && 

		return
