from temperature_converter import Temperature

class Main():
    def __init__(self):
        temp = Temperature()
        while True:
            print("Options:")
            print("1) Set temperature")
            print("2) Convert to Celsius")
            print("3) Convert to Fahrenheit")
            print("4) Convert to Kelvin")
            print("0) Exit program")
            choices = int(input("your choices: "))
            if choices == 1:
                enter = int(input("Enter temperature: "))
                temp.setTemperature(enter)
                print(f"Temperature set to {enter}")
            elif choices == 2:
                print(f"Temperature in Celsius: {temp.toCelsius()}")
            elif choices == 3:
                print(f"Temperature in Fahrenheit: {temp.toFahrenheit()}")
            elif choices == 4:
                print(f"Temperature in Kelvin: {temp.toKelvin()}")
            elif choices == 0:
                print("Program ending.")
                break
if __name__ == "__main__":
    app = Main()

