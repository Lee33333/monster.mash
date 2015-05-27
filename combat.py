import random

#This the base class for characters and monsters

class Combat:
	dodge_limit = 6
	attack_limit = 6

	def dodge(self):
		#dodge method returns a random event outcome

		roll = random.randint(1, self.dodge_limit)
		return roll > 4

	def attack(self):
		#attack method returns a random event outcome

		roll = random.randint(1, self.attack_limit)
		return roll > 4
