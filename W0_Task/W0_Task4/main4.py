from coin_acceptor_2 import CoinAcceptor2

class Main:
    def __init__(self):
        coin = CoinAcceptor2()
        while True:
            value = float(input("your choices: "))
            if value == -1:
                print("Thank you! Goodbye!")
                break
            elif value == 0:
                coins, total = coin.returnCoins()
                if coins > 0:
                    print(f"Returned {coins} coins")
                    print(f"Total value: ${total:.2f}")
                else:
                    print("No coins to return")
            elif value > 0:
                coin.insertCoin(value)
                print(f"Added ${value:.2f}")
                print(f"have {coin.getAmount()} - {coin.getValue()}")
            else:
                print("Value must be positive!")
if __name__ == "__main__":
    app = Main()