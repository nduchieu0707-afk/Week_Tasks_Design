from wallet import WalletCrypter

def main():
    all_wallet = []
    while True:
        choices = int(input("your choices: "))
        if choices == 1:
            name = str(input("your name: "))
            all_wallet.append(WalletCrypter(name))
        elif choices == 2:
            if not all_wallet:
                print("please create your wallet:")
                continue
            what_wallet = int(input("what wallet: "))
            amount = int(input("your money: "))
            if all_wallet[what_wallet].deposit(amount):
                print("success")
            else:
                print("not found")
        elif choices == 3:
            if not all_wallet:
                print("please create your wallet:")
                continue
            what_wallet = int(input("what wallet: "))
            amount = int(input("your money withdraw: "))
            if all_wallet[what_wallet].withdraw(amount):
                print("widthdraw success")
            else:
                print("not found")
        elif choices == 4:
            if not all_wallet:
                print("please create your wallet:")
                continue
            what_wallet = int(input("what wallet: "))
            print (f"{all_wallet[what_wallet].check_balance()}")
        
        elif choices == 5:
            if not all_wallet:
                print("please create your wallet:")
                continue
            what_wallet = int(input("what wallet: "))
            print (f"{all_wallet[what_wallet].history()}")

        elif choices == 6:
            break
main()