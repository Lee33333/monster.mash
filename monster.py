import random

from combat import Combat


COLORS = ["yellow", "red", "blue", "green"]

#Monster inherits from combat class
class Monster(Combat):

	#establishes some default attributes
	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'roar'

	def __init__(self, **kwargs):
		#generates default levels to begin
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.max_experience, self.max_experience)
		self.color = random.choice(COLORS)

		#reads in any additional variables set at initiation
		for key, value in kwargs.items():
			setattr(self,key, value)

	#prints description
	def __str__(self):
		return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
											self.name,
											self.hit_points,
											self.experience)

	def battlecry(self):
		return self.sound.upper()

#inherits from monster, adn overrides some attributes
class Goblin(Monster):
	max_hit_points = 3
	max_experience =2
	name = "Goblin"
	sound = 'squeak'		

#inherits from monster, adn overrides some attributes
class Troll(Monster):
	max_hit_points = 5
	min_hit_points = 3
	max_experience = 6
	name = "Troll"
	sound = 'growl'

#inherits from monster, adn overrides some attributes
class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	name = "Dragon"
	sound = 'raaaaaaaaaaaaaar'