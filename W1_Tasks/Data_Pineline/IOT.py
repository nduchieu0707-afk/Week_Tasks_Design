import csv
import os
from cryptography.fernet import Fernet

class IoTDevice():
    def __init__(self, deviceId, location, data):
        self.deviceId = deviceId
        self.location = location
        self.data = data

class TemperatureSensor(IoTDevice):
    def __init__(self, deviceId, location, data):
        super().__init__(deviceId, location, data)
        self.type = "Temperature"

class HumiditySensor(IoTDevice):
    def __init__(self, deviceId, location, data):
        super().__init__(deviceId, location, data)
        self.type = "Humidity"

class MotionSensor(IoTDevice):
    def __init__(self, deviceId, location, data):
        super().__init__(deviceId, location, data)
        self.type = "Motion"

def serialize(devices, filename="iot_data.csv"):
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Type", "DeviceID", "Location", "Data"])
            for d in devices:
                writer.writerow([d.type, d.deviceId, d.location, d.data])
        print("successfully!")
    except:
        print("failed!")

def deserialize(filename="iot_data.csv"):
    devices = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) == 4:
                    t, id, loc, data = row
                    if t == "Temperature":
                        devices.append(TemperatureSensor(id, loc, data))
                    elif t == "Humidity":
                        devices.append(HumiditySensor(id, loc, data))
                    elif t == "Motion":
                        devices.append(MotionSensor(id, loc, data))
        print("successfully!")
        return devices
    except:
        print("failed!")
        return []

def encrypt(filename="iot_data.csv"):
    try:
        key = Fernet.generate_key()
        with open("key.key", 'wb') as f:
            f.write(key)
        
        fernet = Fernet(key)
        with open(filename, 'rb') as f:
            data = f.read()
        
        with open(filename + ".enc", 'wb') as f:
            f.write(fernet.encrypt(data))
        print("successfully!")
    except:
        print("failed!")

def decrypt(filename="iot_data.csv.enc"):
    try:
        with open("key.key", 'rb') as f:
            key = f.read()
        
        fernet = Fernet(key)
        with open(filename, 'rb') as f:
            data = f.read()
        
        with open("iot_data_decrypted.csv", 'wb') as f:
            f.write(fernet.decrypt(data))
        print("successfully!")
    except:
        print("failed!")

def main():
    devices = []
    
    while True:
        print("\n=== IoT DEVICE MANAGEMENT ===")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")
        
        try:
            choice = int(input("Choice: "))
            
            if choice == 1:
                print("\n1. Temperature | 2. Humidity | 3. Motion")
                types = int(input("Type: "))
                id = input("Device ID: ")
                loc = input("Location: ")
                data = input("Data: ")
                
                if types == 1:
                    devices.append(TemperatureSensor(id, loc, data))
                elif types == 2:
                    devices.append(HumiditySensor(id, loc, data))
                elif types == 3:
                    devices.append(MotionSensor(id, loc, data))
                print("Added!")
            
            elif choice == 2:
                if devices:
                    serialize(devices)
                else:
                    print("No devices!")
            
            elif choice == 3:
                devices = deserialize()
            
            elif choice == 4:
                encrypt()
            
            elif choice == 5:
                decrypt()
            
            elif choice == 0:
                print("Bye!")
                break
            
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Enter a number!")
        except:
            print("Error!")

if __name__ == "__main__":
    main()
