class Entity():
    def __init__(self, name):
        self.name = name

class Player(Entity):
    def interact(self):
        return (f"Player {self.name} is fighting")
    
class NPC(Entity):
    def interact(self):
        return (f"NPC {self.name} is talking")
    
class Object(Entity):
    def interact(self):
        return (f"Object {self.name} is being used")