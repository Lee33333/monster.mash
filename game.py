import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game:
	def setup(self):
		#instance of character instantiated as player
		self.player = Character()
		#monsters instantiated
		self.monsters = [
			Goblin(),
			Troll(),
			Dragon(),
		]
		self.monster = self.get_next_monster()

	def get_next_monster(self):
		#will get monsters, if not replace IndexError with None
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None

	def monster_turn(self):
		#check to see if monster attacks
		if self.monster.attack():
		#if so, tell the player
			print "{} attacks".format(self.monster)
			#check if the player wants to dodge
			if raw_input("Dodge? Y/N ").lower == 'y':
			#if so, see if dodge is successful
				if self.player.dodge():
				#if it is, move on
					print "{} dodged".format(self.monster)
				#if its not, remove player hit point
				else:
					print "{} got you".format(self.monster)
					self.player.hit_points -= 1
			else:
				print "{} hit you for 1 point!".format(self.monster)
				self.player.hit_points -= 1
		# if the monster isn't attacking, tell the player
		else:
			print "{} did not attack".format(self.monster)

	def player_turn(self):
		#let the player attack, rest, or quit
		decision = raw_input("[a]ttack, [r]est, or [q]uit?").lower()
		#if they attack:
		if decision == "a":
			#see if attack is successful
			print "You're attacking {}".format(self.monster)
			if self.player.attack():
				#if so, see if the monster dodges
				if self.monster.dodge():
					#if dodged, print that
					print "{} dodged".format(self.monster)
				#if not dodged, subtract the right number of hit point from monster
				else:
					self.monster.hit_points = self.monster.hit_points -1
					print "{} lost hit point".format(self.monster)
				#if not a good attack, tell player
			else:
				print "You missed!"
		#if they rest:
		elif decision == "r":
			self.player.rest()
			print "Player rested"
			#call player.rest() method
		#if they quit, exit the game
		elif decision == "q":
			sys.exit()
		#if they pick anything else, re-run this method
		else: 
			return self.player_turn()

	def cleanup(self):
		#if the monster has no more hit points:
		if self.monster.hit_points <= 0:
			#up the players experience
			self.player.experience += self.monster.experience
			#print a message
			print "{} defeated!".format(self.monster)
			#get a new monster
			self.monster = self.get_next_monster()

	def __init__(self):
		self.setup()

		while self.player.hit_points and (self.monster or self.monsters):
			print "\n" +"=" * 20
			print self.player
			self.monster_turn()
			print "\n" +"-" * 20
			self.player_turn()
			self.cleanup()

		if self.player.hit_points:
			print "You win!"
		elif self.monsters or self.monster:
			print "You lose :("		
		sys.exit()

Game()






