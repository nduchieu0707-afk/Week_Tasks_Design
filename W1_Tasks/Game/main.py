from game import Archer, Saber, Caster
from abc import ABC

servants = []

def simulate_battle():
    for s in servants:
        print(s.attack())
        print(s.defend())

def main():
    while True:
        choices = int(input("your choices: "))
        if choices == 1:
            name = str(input("name: "))
            classes = int(input("your classes: "))
            if classes == 1:
                servants.append(Archer(name))
            elif classes == 2:
                servants.append(Saber(name))
            elif classes == 3:
                servants.append(Caster(name))
        elif choices == 2:
            simulate_battle()
        elif choices == 0:
            break
main()
