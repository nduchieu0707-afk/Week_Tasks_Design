from Smart_house import Smartlight, SmartDevice, SmartThermo

def main():
    Smarts = []
    while True:
        choices = int(input("your choices: "))
        if choices == 1:
            types = int(input("your types: "))
            name = int(input("your name: "))
            if types == 1:
                Smarts.append(Smartlight(name))
            elif types == 2:
                Smarts.append(SmartDevice(name))
            elif types == 3:
                Smarts.append(SmartThermo(name))
        elif choices == 2:
            for s in Smarts:
                print(s.operate())
        elif choices == 0:
            break
main()