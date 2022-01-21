import Weapons_and_Armour

class Weapon:
    """A Default weapon class that gives all the attributes to the Attacks and minor Defence stats to the Player as well as an Enemy."""
    def __init__(self, attack, defence):
        self.at = attack
        self.de = defence

        Weapons_and_Armour.list1.append(self.__name__)

class Entity:
    """An entity class that refers to any character on screen one wishes to interact with, by either fighting or talking to."""
    def __init__(self, health = int):
        self.health = health

class Armour:
    """A default armour class that has a set attributes to give to any entity it is equipped to."""
    def __init__(self, health_boost, defence, attack):
        self.he = health_boost
        self.de = defence
        self.at = attack
    
    def equip(self, ent = Entity):
        """Equips the Armour on a specific entity, thereby adding up on the entity's attributes."""
        ent.armour = self

class Enemy(Entity):
    """An opposing party one must obliterate to advance in the game. Try to minimise damage against them or you will have to use accessories to heal."""
    def __init__(self, weapon = Weapon):
        super().__init__(100)
        self.weapon = weapon
        self.de = 5
        self.at = 7

    
class Neutral(Entity):
    """A character that would not inherently be aggressive to players and can only be provoked to attack the player."""
    def __init__(self, weapon = Weapon):
        super().__init__(100)
        self.weapon = weapon

class Player(Entity):
    """A class to contain the Player's basic information and progress."""
    def __init__(self):
        super().__init__(100)

class Mage(Player):
    """The mage class is extremely effective at dealing high amounts of damage but at the expense of their defence which usually renders them vulnerable. Choose your next steps very carefully."""
    def __init__(self, weapon = Weapon):
        super().__init__()
        self.de = 10
        self.at = 20
        
class Knight(Player):
    """The Knight class is skilled with both the shield and the sword, so you do not have to worry too much about taking damage or dealing any in return as long as you play reasonably."""
    def __init__(self, weapon = Weapon):
        super().__init__()
        self.de = 15
        self.at = 25
        self.weapon = weapon

class Castellan(Player):
    """The Castellans are a big tank for all damage to be absorbed by. The Castellan's mighty defence makes its attacks weak and slow, but with a massive base defence it is difficult to die."""
    def __init__(self, weapon = Weapon):
        super().__init__()
        self.de = 20
        self.at = 10
        self.weapon = weapon


def spawn(entity = Entity, weapon = Weapon):
    ent = entity(weapon)