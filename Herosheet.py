class Hobbit(object):
	def __init__(self, name):
		self.name = name
		self.race = "Hobbit"
		self.power = 3
		self.defense = 0
		self.speed = 3
		self.stealth = 9
		self.magic = 1
		self.health = 10
		self.home = "The Shire"

class Dwarf(object):
	def __init__(self, name):
		self.name = name
		self.race = "Dwarf"
		self.power = 6
		self.defense = 3
		self.speed = 3
		self.stealth = 2
		self.magic = 1
		self.health = 18
		self.home = "The Misty Mountains"

class Rohan(object):
	def __init__(self, name):
		self.name = name
		self.race = "Man of Rohan"
		self.power = 8
		self.defense = 1
		self.speed = 5
		self.stealth = 3
		self.magic = 1
		self.health = 15
		self.home = "Rohan"

class Gondor(object):
	def __init__(self, name):
		self.name = name
		self.race = "Man of Gondor"
		self.power = 7
		self.defense = 2
		self.speed = 4
		self.stealth = 3
		self.magic = 1
		self.health = 15
		self.home = "Gondor"

class Rivendell(object):
	def __init__(self, name):
		self.name = name
		self.race = "Elf of Rivendell"
		self.power = 5
		self.defense = 2
		self.speed = 6
		self.stealth = 3
		self.magic = 3
		self.health = 20
		self.home = "Rivendell"

class Lothlorien(object):
	def __init__(self, name):
		self.name = name
		self.race = "Elf of Lothlorien"
		self.power = 4
		self.defense = 1
		self.speed = 5
		self.stealth = 3
		self.magic = 5
		self.health = 19
		self.home = "Lothlorien"