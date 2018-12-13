"""This module contains a class that allows to model random walks"""

# import
from random import choice


class RandomWalk:
	"""A model of random walks generator"""
	
	def __init__(self, num_points=5000):
		"""Initializes random walk"""
		self.num_points = num_points  # how many points will random walk consist of
		
		# all random walks start from point (0,0)
		self.x_values = [0]
		self.y_values = [0]

	@staticmethod
	def get_step():
		"""Gets a value and direction of the next step of a random walk"""
		direction = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4, 5])  # each next step in a random walk can be from 1 to 5 length
		step = direction*distance
		return step
		
	def fill_walk(self):
		"""Calculates coordinates of all points of a random walk"""

		while len(self.x_values) < self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()
			
			# reject zero movement
			if x_step == 0 and y_step == 0:
				continue
				
			# calculate x and y of the following random walk step
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			self.x_values.append(next_x)
			self.y_values.append(next_y)
