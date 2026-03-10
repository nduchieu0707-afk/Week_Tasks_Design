import csv
import json
from datetime import datetime

class IoTDevice:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"{self.device_id} at {self.location}"

class TemperatureSensor(IoTDevice):
    def __init__(self, device_id, location, temperature):
        super().__init__(device_id, location)
        self.temperature = temperature
        self.data = {"temperature": temperature}

class HumiditySensor(IoTDevice):
    def __init__(self, device_id, location, humidity):
        super().__init__(device_id, location)
        self.humidity = humidity
        self.data = {"humidity": humidity}

class MotionSensor(IoTDevice):
    def __init__(self, device_id, location, motion_detected):
        super().__init__(device_id, location)
        self.motion_detected = motion_detected
        self.data = {"motion_detected": motion_detected}

class CSVHandler:
    @staticmethod
    def save_to_csv(devices, filename="devices.csv"):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['type', 'id', 'location', 'data'])
            
            for device in devices:
                writer.writerow([
                    device.__class__.__name__,
                    device.device_id,
                    device.location,
                    json.dumps(device.data)
                ])
        print(f"Saved {len(devices)} devices to {filename}")
    
    @staticmethod
    def load_from_csv(filename="devices.csv"):
        devices = []
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                device_type = row['type']
                device_id = row['id']
                location = row['location']
                data = json.loads(row['data'])
                
                if device_type == "TemperatureSensor":
                    device = TemperatureSensor(device_id, location, data['temperature'])
                elif device_type == "HumiditySensor":
                    device = HumiditySensor(device_id, location, data['humidity'])
                elif device_type == "MotionSensor":
                    device = MotionSensor(device_id, location, data['motion_detected'])
                else:
                    continue
                
                devices.append(device)
        print(f"Loaded {len(devices)} devices from {filename}")
        return devices

class SimpleEncryptor:
    @staticmethod
    def encrypt_file(input_file, output_file, key="secret"):
        with open(input_file, 'rb') as f:
            data = f.read()
        
        key_bytes = key.encode()
        encrypted = bytearray()
        for i, byte in enumerate(data):
            encrypted.append(byte ^ key_bytes[i % len(key_bytes)])
        
        with open(output_file, 'wb') as f:
            f.write(encrypted)
        print(f"Encrypted {input_file} to {output_file}")
    
    @staticmethod
    def decrypt_file(input_file, output_file, key="secret"):
        SimpleEncryptor.encrypt_file(input_file, output_file, key)
        print(f"Decrypted {input_file} to {output_file}")