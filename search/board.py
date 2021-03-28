from .token import Token
from .util import *

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

	def find_token_paths(self):
		for my_token in self.upper_tokens:
			extra_block = []
			for tokens in self.lower_tokens:
				if (my_token.category == "s") & (tokens.category == "r"):
					extra_block.append(tokens.position)
				elif (my_token.category == "r") & (tokens.category == "p"):
					extra_block.append(tokens.position)
				elif (my_token.category == "p") & (tokens.category == "s"):
					extra_block.append(tokens.position)
			my_token.get_viable_target(self.lower_tokens)
			my_token.get_nearest_target()
			my_token.get_token_path(self.block_tokens, extra_block)

	def move_tokens(self):
		all_current_location = []
		for token in self.upper_tokens:
			all_current_location.append(token.position)

		next_move_list = []
		for token in self.upper_tokens:
			
			print(token.path)
			next_position = token.path[0]

			#check is swing is possible and optimal
			possible_move = token.check_swing(all_current_location)
			if (possible_move != None):
				next_position = possible_move

			next_move_list.append(next_position);
		
		#if next_move_list cotains duplicate, check for clash.
		if (any(next_move_list.count(element) > 1 for element in next_move_list)):
			(first, second) = find_duplicate(next_move_list)
			#if both have different type, then change the path for the second one
			if (self.upper_tokens[first].category != self.upper_tokens[second].category):
				first_token = self.upper_tokens[first]
				second_token = self.upper_tokens[second]
				second_token.get_token_path(self.block_tokens, [next_move_list[first]])
				next_move_list[second] = second_token.path[0]

		#iterate through the upper tokens to move
		for iterator in range(len(self.upper_tokens)):
			current_token = self.upper_tokens[iterator]
			
			if distance(next_move_list[iterator], current_token.position) > 1:
				current_token.swing(next_move_list[iterator], self.turn)
			else:
				current_token.slide(next_move_list[iterator], self.turn)

			#iterate through viable target to check if the token defeats any token
			for j in range(len(current_token.viable_target)):

				#if yes, then remove the enemy token
				if current_token.viable_target[j].position == next_move_list[iterator]:
					del current_token.viable_target[j]

					#iterate through lower tokens to remove enemy token
					for i in range(len(self.lower_tokens)):
						if (self.lower_tokens[i].position == next_move_list[iterator]):
							current_token.target = None
							del self.lower_tokens[i]
							break
					break

