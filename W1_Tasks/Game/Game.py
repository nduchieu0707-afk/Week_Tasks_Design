from abc import ABC, abstractmethod

class Characters(ABC):
    def __init__(self, name):
        self.name = name
        self.health = 100

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class Archer(Characters):
    def attack(self):
        self.damagearcher = 30
        return (f"{self.name} attack with damage {self.damagearcher}")

    def defend(self):
        self.defendarcher = 10
        return (f"{self.name} defend with plot {self.defendarcher}")
    
class Saber(Characters):
    def attack(self):
        self.attacksaber = 25
        return (f"{self.name} attack with damage {self.attacksaber}")
    
    def defend(self):
        self.defendsaber = 15
        return (f"{self.name} defend with plot {self.defendsaber}")
    
class Caster(Characters):
    def attack(self):
        self.attackcaster = 10
        return (f"{self.name} attack with damage {self.attackcaster}")
    def defend(self):
        self.defendcaster = 30
        return (f"{self.name} defend with plot {self.defendcaster}")
    
