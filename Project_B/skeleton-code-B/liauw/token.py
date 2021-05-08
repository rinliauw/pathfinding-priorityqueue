from .util import *

class Token:
#class constructor
	def __init__(self, category, position):
		self.position = position
		self.category = category
		self.viable_target = []
		self.possible_moves = []
	
	def get_category(self):
		return self.category
	
	#iterate through the lower token list, and get all viable target
	def get_viable_target(self, enemy_list):
		self.viable_target = []
		for enemy in enemy_list:
			if enemy in self.viable_target:
				continue
			if (self.category == 'r') & (enemy.category == 's'):
				self.viable_target.append(enemy)
			elif (self.category == 's') & (enemy.category == 'p'):
				self.viable_target.append(enemy)
			elif (self.category == 'p') & (enemy.category == 'r'):
				self.viable_target.append(enemy)

	#get the nearest target
	def get_nearest_target(self):
		if (len(self.viable_target) > 0):
			minimum = 0
			for i in range(len(self.viable_target)):
				if distance(self.viable_target[i].position, self.position) < distance(self.viable_target[minimum].position, self.position):
					minimum = i
			self.target = self.viable_target[minimum].position

	#this function appends position that are possible by swing action
	def get_swing_moves(self, ally_tokens_location):
		nearby_ally = []
		neighbours = get_neighbours(self.position)
		for location in ally_tokens_location:
			if location in neighbours:
				nearby_ally.append(location)
		if (nearby_ally == []):
			return None
		else:
			for ally in nearby_ally:
				swing_moves = get_swing_position(self.position, ally)
				for move in swing_moves:
					self.possible_moves.append(move)

	def get_nearest_ally(self, ally_list):
		# set the shortest distance to index 0 of ally_list
		shortest_distance = 0

		#if ally_list[0] is itself, then set the index to 1
		if distance(self.position, ally_list[0].position) == 0:
			shortest_distance = 1

		#find the shortest distance
		for i in range(len(ally_list)):
			if (distance(self.position, ally_list[i].position) == 0):
				continue
			if (distance(self.position, ally_list[i].position) < distance(self.position, ally_list[shortest_distance].position)):
				shortest_distance = i

		return ally_list[shortest_distance]
	
	def generate_all_slide():
		neighbours = get_neighbours(self.position)
		for pos in neighbours:
			possible_moves.append(pos)
	