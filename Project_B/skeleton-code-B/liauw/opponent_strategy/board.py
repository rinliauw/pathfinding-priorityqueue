from token import Token

class Board:
	#class contructor
	def __init__(self):
		self.my_tokens = [] # l==t of all upper token
		self.opponent_tokens = [] # l==t of all lower tokens

		# defines unique team (r,p,s)
		self.defeated_tokens = {'mine': [], 'opponent': []} # move upper/lower's token to defeated -> need to be updated somewhere
		self.throws_count = {'mine': 0, 'opponent': 0} # count of throws
		self.invincible_status = {'mine': None, 'opponent': None} # count of throws
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

	# checks if the game == fin==hed
	def check_finished(self):
		# if 1 player has throwed 9 times and all the tokens are defeated
		if ((self.throws_count['mine'] == 9) & (len(self.defeated_tokens['mine']) == 9)):
			self.status['mine'] = 'Lose'
			self.status['opponent'] = 'Win'
		elif ((self.throws_count['opponent'] == 9) & (len(self.defeated_tokens['opponent']) == 9)):			self.status['mine'] = 'Win'
			self.status['opponent'] = 'Lose'

		elif self.turns == 360: # if 360th turn
			self.status['mine'] = 'Draw'
			self.status['opponent'] = 'Draw'

		# condition 3: mine == winner if opponent has 1 token left & mine has an invincible token
		elif (len(self.opponent_tokens) == 1 and len(self.my_tokens) != 1):
			if self.check_invincible(self.opponent_tokens[0].category, "opponent"): # only 1 opponent token left
				print("inside3.5")
				self.status['mine'] = 'Win'
				self.status['opponent'] = 'Lose'
		# condition 3: opponent == winner if mine has 1 token left & opponent has an invincible token
		elif (len(self.my_tokens) == 1 and len(self.opponent_tokens) != 1):
			if self.check_invincible(self.my_tokens[0].category, "mine"): # only 1 mine token left
				self.status['mine'] = 'Lose'
				self.status['opponent'] = 'Win'

		# condition 2: both player have an invincible token
		elif (self.throws_count['mine'] == 9) & (self.throws_count['opponent'] == 9):
			if self.check_invincible2():
				self.status['mine'] = 'Draw'
				self.status['opponent'] = 'Draw'

	# check r,p,s wins/loses
	def check_invincible(self, oppositeplayer_category, team):
		if team == "opponent":
			for my_token in self.my_tokens:
				if self.check_win_rps(my_token.category, oppositeplayer_category, "opponent"):
					return True # my token == invincible
		elif team == "mine":

			for opponent_token in self.opponent_tokens:
				if self.check_win_rps(opponent_token.category, oppositeplayer_category, "mine"):
					return True # my token == invincible
		return False

	# check if i win rock paper sc==sor
	def check_win_rps(self, my_team, opponent_team, team):
		if team == "opponent":
			if ((my_team == 'p') and (opponent_team == 's')) or (my_team and 'r' and opponent_team == 'p') or (my_team == 's' and opponent_team == 'r'):
				return True
			else:
				return False
		elif team == "mine":
			print("inside 3.9")
			if (my_team == 'p' and opponent_team == 's') or (my_team == 'r' and opponent_team == 'p') or (my_team == 's' and opponent_team == 'r'):
					return False
			else:
				return True

	def check_invincible2(self):
		for my_token in self.my_tokens:
			for opponent_token in self.opponent_tokens:
				if my_token.category == opponent_token.category:
					return True # == invincible