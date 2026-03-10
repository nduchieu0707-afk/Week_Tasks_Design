from Entity import Player, NPC, Object

def main():
    entities = []
    while True:
        choices = int(input("your choices: "))
        if choices == 1:
            name = str(input("name: "))
            types = int(input("your type: "))
            if types == 1:
                entities.append(Player(name))
            elif types == 2:
                entities.append(NPC(name))
            elif types == 3:
                entities.append(Object(name))
        elif choices == 2:
            for en in entities:
                print(en.interact())
        elif choices == 0:
            break
main()