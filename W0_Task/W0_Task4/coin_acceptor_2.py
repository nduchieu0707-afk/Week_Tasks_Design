class CoinAcceptor2:
    def __init__(self):
        self.amount = 0
        self.value = 0.0
    def insertCoin(self, insert: float):
        self.amount += 1
        self.value += insert
    def getAmount(self):
        return self.amount
    def getValue(self):
        return self.value
    def returnCoins(self):
        returncoints = (self.amount, self.value)
        self.amount = 0
        self.value = 0.0
        return returncoints