from counter import Counter

class Main():
    def __init__(self):
        own_counter = Counter()
        while True:
            print("Options:")
            print("1) Add count")
            print("2) Get count")
            print("3) Zero count")
            print("0) Exit program")
            choices = int(input("your choices: "))
            if choices == 1:
                print(f"Current Count {own_counter.addCount()}")
            elif choices == 2:
                own_counter.getCount()
                print("Count increased")
            elif choices == 3:
                own_counter.ZeroCount()
                print("Count zeroed")
            elif choices == 0:
                break
if __name__ == "__main__":
    app = Main()