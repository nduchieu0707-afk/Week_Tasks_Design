from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self):
        coin = CoinAcceptor()
        while True:
            print("1 - Insert coin")
            print("2 - Show coins")
            print("3 - Return coins")
            print("0 - Exit program")
            choices = int(input("your choices: "))
            if choices == 1:
                Insert = int(input("your choices: "))
                coin.insertCoin(Insert)
            elif choices == 2:
                print(f"Currently {coin.getAmount()} coins in coin acceptor")
            elif choices == 3:
                print(f"Coin acceptor returned {coin.returnCoins()} coins")
            elif choices == 0:
                print("Program ending")
                break
if __name__ == "__main__":
    app = Main()