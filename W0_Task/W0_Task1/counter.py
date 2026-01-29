class Counter:
    def __init__(self):
        self.count = 0
        
    def addCount(self):
        return self.count

    def getCount(self):
        self.count += 1

    def ZeroCount(self):
        self.count = 0