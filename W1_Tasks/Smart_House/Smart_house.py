class SmartHouse():
    def __init__(self, name):
        self.name = name
        self.status = "off"

class Smartlight(SmartHouse):
    def operate(self):
        if self.status == "off":
            self.status = "on"
        else:
            self.status = "off"
        return (f"{self.name} turned {self.status}")
    
class SmartThermo(SmartHouse):
    def __init__(self, name):
        super().__init__(name)
        self.thermo = 22
    def operate(self):
        if self.status == "off":
            self.status = "on"
        else:
            self.status = "off"
        return (f"{self.name} set as {self.thermo}")
    
class SmartDevice(SmartHouse):
    def __init__(self, name):
        super().__init__(name)
        self.locked = True
    def operate(self):
        self.locked = not self.locked
        if self.locked:
            self.status = "locked"
        else:
            self.status = "unlocked"
        return (f"{self.name} is {self.status}")

