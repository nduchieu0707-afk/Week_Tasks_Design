from datetime import datetime
import uuid

class WalletCrypter():
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.id = uuid.uuid4[::8]
        self.save = []

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self.save.append(f"{self.balance}")
        else:
            print("Hell nah")

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            self.save.append(f"{self.balance}")
        else:
            print("Hell nah")

    def check_balance(self):
        return (f"{self.id} - {self.balance}")
    
    def transaction_history(self):
        if self.save:
            return self.save
        else:
            print("no wallet")
