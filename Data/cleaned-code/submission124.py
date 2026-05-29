class MobileDevice:
    def __init__(self, brand, model, os_version, battery_capacity):
                                                                                      
        self.brand = brand
        self.model = model
        self.os_version = os_version
        self.battery_capacity = battery_capacity

    def display_info(self):
                                                               
        print(f"Brand: {self.brand}, Model: {self.model}, OS Version: {self.os_version}, Battery: {self.battery_capacity}mAh")

def add_device(devices, brand, model, os_version, battery_capacity):
                                          
    device = MobileDevice(brand, model, os_version, battery_capacity)
    devices.append(device)

def list_devices(devices):
                                    
    for device in devices:
        device.display_info()

def main():
                                            
    devices = []
    add_device(devices, "Xiaomi", "Mi 11", "Android 11", 4600)
    add_device(devices, "OnePlus", "9 Pro", "Android 11", 4500)
    
    print("List of mobile devices with battery info:")
    list_devices(devices)

if __name__ == "__main__":
    main()
    