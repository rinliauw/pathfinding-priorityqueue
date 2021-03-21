from .priorityQueue import PriorityQueue
from .hexpath import HexPath
from .util import *

class Token:

	#class constructor
	def __init__(self, position, category, team):
		self.position = position
		self.category = category
		self.team = team
		self.path = None
		self.target = None
		self.viable_target = []

	def get_category(self):
		return self.category
	
	def get_viable_target(self, enemy_list):
		for enemy in enemy_list:
			if (self.category == 'r') & (enemy.category == 's'):
				self.viable_target.append(enemy)
			elif (self.category == 's') & (enemy.category == 'p'):
				self.viable_target.append(enemy)
			elif (self.category == 'p') & (enemy.category == 'r'):
				self.viable_target.append(enemy)


	def get_nearest_target(self):
		for target in self. viable_target:
			target_position = target.position
			if self.target == None:
				self.target = target_position
			elif distance(self.position, self.target) > distance(self.position, target_position):
				self.target = target_position

	def get_token_path(self, block_tokens):
		blocked_hex = []
		for tokens in block_tokens:
			blocked_hex.append(tokens.position)

		open_hex = PriorityQueue()		#a priority queue for exploring the map
		close_hex = []					#a list of coordinate that has already been explored

		start = HexPath(self.position)
		start.set_f_cost(0)

		open_hex.insert(start)

		while not open_hex.isEmpty():
			#pop the current hex and get it's neighbours
			current_hex = open_hex.pop()
			close_hex.append(current_hex.position)
			child_list = get_neighbours(current_hex.position)

			if current_hex.position == self.target:
					break

			#set the parents of all the neighbours to the current hex
			for child in child_list:
				child_hex = HexPath(child)

				#if the child hex is blocked or already been explored, then skip it
				if (child_hex.position in blocked_hex) | (child_hex.position in close_hex):
					continue

				#calculate the f cost of the child and set the parent of the child to the current hex	
				current_f_cost = calc_f_cost(start.position, child_hex.position, self.target)
				child_hex.set_f_cost(current_f_cost)
				child_hex.set_parent(current_hex)

				#if the child already in open_hex, but have lower updated f cost
				if open_hex.contains(child_hex):
					if (open_hex.get_priority(child_hex) > current_f_cost):
						open_hex.update_priority(child_hex, current_f_cost)

				#if the child is not in open_hex
				if not (open_hex.contains(child_hex)):
					open_hex.insert(child_hex)

		while current_hex.parent != None:
			print(current_hex.position)
			current_hex = current_hex.parent
		print(current_hex.position)