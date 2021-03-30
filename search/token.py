from .priorityQueue import PriorityQueue
from .hexpath import HexPath
from .util import *

class Token:

	#class constructor
	def __init__(self, position, category, team):
		self.position = position
		self.category = category
		self.team = team
		self.path = []
		self.target = None
		self.viable_target = []
		self.finished = False

	def get_category(self):
		return self.category

	# considers all upper token's enemies
	def get_viable_target(self, enemy_list):
		for enemy in enemy_list:
			if enemy in self.viable_target:
				continue
			if (self.category == 'r') & (enemy.category == 's'):
				self.viable_target.append(enemy)
			elif (self.category == 's') & (enemy.category == 'p'):
				self.viable_target.append(enemy)
			elif (self.category == 'p') & (enemy.category == 'r'):
				self.viable_target.append(enemy)

	# finds nearest enemy of each token by calculating the Manhattan distance
	def get_nearest_target(self, upper_tokens):
		#what to do when token is done
		if ((self.target == None) | (self.target == self.position)) & (self.viable_target == []):
			self.viable_target = upper_tokens.copy()
			minimum = 0
			for i in range(len(self.viable_target)):
				if self.position != self.viable_target[i].position:
					print(self.viable_target[i].position)
					if distance(self.viable_target[i].position, self.position) < distance(
							self.viable_target[minimum].position, self.position):
						minimum = i
			self.target = self.viable_target[minimum].position
			return
		# finds nearest target (excluding blocks) when token hasn't set target
		elif (self.target == None) & (len(self.viable_target) > 0):
			minimum = 0
			for i in range(len(self.viable_target)):
				if distance(self.viable_target[i].position, self.position) < distance(self.viable_target[minimum].position, self.position):
					minimum = i
			self.target = self.viable_target[i].position
		# updates target if there is other target that is closer to current token position
		else:
			for target in self.viable_target:
				if distance(self.target, self.position) > distance(target.position, self.position):
					self.target = target.position

	# performs A* algorithm
	def get_token_path(self, block_tokens, extra_block):
		blocked_hex = []
		self.path = []

		if self.target == self.position:
			self.path.append(self.position)
			return

		# collectively append blocked tokens
		for tokens in block_tokens:
			blocked_hex.append(tokens.position)
		for position in extra_block:
			blocked_hex.append(position)

		open_hex = PriorityQueue()		# a priority queue for exploring the map
		close_hex = []					# a list of coordinate that has already been explored

		start = HexPath(self.position)
		start.set_f_cost(0)
		start.g_cost = 0

		open_hex.insert(start)

		while not open_hex.isEmpty():
			# pop the current hex with lowest f_cost and get it's neighbours
			current_hex = open_hex.priority_pop()
			close_hex.append(current_hex.position)
			child_list = get_neighbours(current_hex.position)

			# target has been found, stop looking
			if current_hex.position == self.target:
				break

			# set the parents of all the neighbours to the current hex
			for child in child_list:
				child_hex = HexPath(child)
				child_hex.g_cost = current_hex.g_cost + 1

				#if the child hex is blocked or already been explored, then skip it
				if (child_hex.position in blocked_hex) | (child_hex.position in close_hex):
					continue

				# calculate the f cost of the child and set the parent of the child to the current hex
				current_f_cost = calc_f_cost(child_hex.position, self.target, child_hex.g_cost)
				child_hex.set_f_cost(current_f_cost)
				child_hex.set_parent(current_hex)

				# if the child already in open_hex, but have lower updated f-cost
				if open_hex.contains(child_hex):
					if (open_hex.get_priority(child_hex) > current_f_cost):
						open_hex.update_priority(child_hex, current_f_cost)

				# if the child is not in open_hex
				if not (open_hex.contains(child_hex)):
					open_hex.insert(child_hex)

		# traverse back the path found by child -> parent
		while current_hex.parent != None:
			self.path.insert(0, current_hex.position)
			current_hex = current_hex.parent

	# performs slide movement
	def slide(self, new_position, turn):
		print_slide(turn, self.position[0], self.position[1], new_position[0], new_position[1])
		self.position = new_position

	# performs swing movement
	def swing(self, new_position, turn):
		print_swing(turn, self.position[0], self.position[1], new_position[0], new_position[1])
		self.position = new_position

	# checks if target still available
	def target_still_available(self, lower_tokens):
		for i in range(len(lower_tokens)):
			if lower_tokens[i].position == self.target:
				return True
		return False

	def check_swing(self, ally_tokens_location):
		# this function returns a coordinate if swing is possible and optimal
		# return None if not possible or not optimal

		nearby_ally = []
		possible_move = []
		neighbours = get_neighbours(self.position)
		for location in ally_tokens_location:
			if location in neighbours:
				nearby_ally.append(location)
		if (nearby_ally == []):
			return None
		else:
			for ally in nearby_ally: # ally position = ally
				swing_moves = get_swing_position(self.position, ally)
				for move in swing_moves:
					possible_move.append(move)
		possible_move.append(self.path[0])

		minimum = 0
		# check the distance of each possible moves, find the smallest distance
		for i in range(len(possible_move)):
			if (distance(possible_move[i], self.target) <= distance(possible_move[minimum], self.target)):
				minimum = i
			#print("distance(possible_move[i], self.target)", distance(possible_move[i], self.target), possible_move[i])
		#print('hi')
		return possible_move[minimum]

