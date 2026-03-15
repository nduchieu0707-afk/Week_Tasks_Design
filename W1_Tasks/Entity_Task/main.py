from entity import Player, NPC, Objects

def main():
    entities = []
    while True:
        choices = int(input("your choices: "))
        if choices == 1:
            name = str(input("your name: "))
            position = int(input("position: "))
            types = int(input("your types: "))
            if types == 1:
                entities.append(Player(name, position))
            elif types == 2:
                entities.append(NPC(name, position))
            elif types == 3:
                entities.append(Objects(name, position))
        elif choices == 2:
            for en in entities:
                print(en.interact())
        elif choices == 0:
            break
main()
