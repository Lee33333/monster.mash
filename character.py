import random

from combat import Combat

class Character(Combat):

	#inherits from combat and establishes some defaults
	attack_limit = 10
	experience = 0
	base_hit_points = 10


	def attack(self):
		#generate a random attack limit
		roll = random.randint(1, self.attack_limit)
		#swords get additional advantages
		if self.weapon == 'sword':
			roll += 1
		#so do axes
		elif self.weapon == 'axe':
			roll += 2
		return roll> 4

	def get_weapon(self):
		# you can select a weapon
		weapon_choice = raw_input("Weapon [S]word, [A]xe, [B]ow ").lower()
		
		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return'sword'
			elif weapon_choice == 'a':
				return 'axe'
			else:
				return 'bow'
		else:
			#ask for weapon again
			return self.get_weapon()

	def __init__(self, **kwargs):
		#initialize a character by asking for name and weapon
		self.name = raw_input("Name: ")
		self.weapon = self.get_weapon()
		self.hit_points = self.base_hit_points

		#read in any additional values form dictionary at initialization
		for key, value in kwargs.items():
			setattr(self, key, value)


	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)

	def rest(self):
		#get one hit point
		if self.hit_points < self.base_hit_points:
			self.hit_points += 1

	def leveled_up(self):
		#is anything else needed here?
		return self.experience >= 5