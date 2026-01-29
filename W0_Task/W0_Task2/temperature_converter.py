class Temperature:
    def __init__(self):
        self.temp = 0.0
    def setTemperature(self, temperature: float):
        self.temp = temperature
    def toCelsius(self):
        return self.temp
    def toFahrenheit(self):
        return (self.temp * 9/5) + 32
    def toKelvin(self):
        return self.temp + 273.15