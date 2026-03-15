class Entity():
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.damage = 10
    def interact(self):
        return (f"{self.name} is attacking with {self.damage}")
    
class NPC(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.diaglogue = "Hello"
    def interact(self):
        return (f"{self.name} is talking {self.diaglogue}")
    
class Objects(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.is_break = True
    def interact(self):
        if self.is_break:
            action = "can be break"
        else:
            action = "cannot break"
        return (f"{self.name} is doing so {action}")
