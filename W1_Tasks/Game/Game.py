from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def defend(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        return f"{self.name} swings a sword for 30 damage!"
    
    def defend(self):
        return f"{self.name} raises shield, defense +20"

class Mage(GameCharacter):
    def attack(self):
        return f"{self.name} casts fireball for 40 damage!"
    
    def defend(self):
        return f"{self.name} creates magic barrier, defense +15"

class Archer(GameCharacter):
    def attack(self):
        return f"{self.name} shoots arrows for 25 damage!"
    
    def defend(self):

        return f"{self.name} dodges quickly, defense +10"
