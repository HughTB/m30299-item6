class SmartDevice():
    def __init__(self):
        self.switchedOn = False

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        return self.switchedOn

class SmartPlug(SmartDevice):
    def __init__(self):
        super().__init__()
        self.consumptionRate = 0

    def __str__(self):
        text = "Plug - "
        text += "on, " if self.switchedOn else "off, "
        text += f"consumption rate: {self.consumptionRate}"
        return text
    
    def getConsumptionRate(self):
        return self.consumptionRate
    
    def setConsumptionRate(self, newConsumptionRate: int):
        if newConsumptionRate >= 0 and newConsumptionRate <= 150:
            self.consumptionRate = newConsumptionRate

washModes = ["Daily wash", "Quick wash", "Eco"]

class SmartWashingMachine(SmartDevice):
    def __init__(self):
        super().__init__()
        self.washMode = "Daily wash"

    def __str__(self):
        text = "Washing Machine - "
        text += "on, " if self.switchedOn else "off, "
        text += f"wash mode: {self.washMode}"
        return text
    
    def getWashMode(self):
        return self.washMode
    
    def setWashMode(self, newWashMode):
        if newWashMode in washModes:
            self.washMode = newWashMode

class SmartHome():
    def __init__(self):
        self.devices = []

    def __str__(self):
        text = "Smart Home - Devices:"
        for device in self.devices:
            text += "\n" + str(device)
        return text

    def getDevices(self):
        return self.devices
    
    def getDeviceAt(self, index: int):
        return self.devices[index]
    
    def addDevice(self, device: SmartDevice):
        self.devices.append(device)

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            if not device.getSwitchedOn():
                device.toggleSwitch()
    
    def turnOffAll(self):
        for device in self.devices:
            if device.getSwitchedOn():
                device.toggleSwitch()

def testSmartPlug():
    plug = SmartPlug()

    plug.toggleSwitch()
    print(plug.getSwitchedOn())
    print(plug.getConsumptionRate())
    plug.setConsumptionRate(60)
    print(plug.getConsumptionRate())
    print(plug)

def testSmartWashingMachine():
    washingMachine = SmartWashingMachine()

    washingMachine.toggleSwitch()
    print(washingMachine.getSwitchedOn())
    print(washingMachine.getWashMode())
    washingMachine.setWashMode("Eco")
    print(washingMachine.getWashMode())
    print(washingMachine)

def testSmartHome():
    smartHome = SmartHome()

    plug1 = SmartPlug()
    plug2 = SmartPlug()
    washingMachine = SmartWashingMachine()

    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    washingMachine.setWashMode("Quick wash")

    smartHome.addDevice(plug1)
    smartHome.addDevice(plug2)
    smartHome.addDevice(washingMachine)

    print(smartHome)
    smartHome.turnOnAll()
    print(smartHome)

print("=== Smart Plug ===")
testSmartPlug()
print("=== Washing Machine (Custom Device) ===")
testSmartWashingMachine()
print("=== Smart Home ===")
testSmartHome()