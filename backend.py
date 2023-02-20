class SmartDevice():
    """Base class for all smart devices, contains methods and properties that all devices must have"""
    def __init__(self):
        """Constructor, sets switchedOn property to false by default"""
        self.switchedOn = False

    def toggleSwitch(self):
        """Toggles the property switchedOn between true and false"""
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        """Returns the value of switchedOn"""
        return self.switchedOn

class SmartPlug(SmartDevice):
    """SmartPlug, inherits from SmartDevice. Contains methods and properties that a smart plug may need to function"""
    def __init__(self):
        """Constructor, sets consumptionRate to 0 by default"""
        super().__init__()
        self.consumptionRate = 0

    def __str__(self):
        """Returns a string containing information about the smart plug"""
        text = "Plug - "
        text += "on, " if self.switchedOn else "off, "
        text += f"consumption rate: {self.consumptionRate}"
        return text
    
    def getConsumptionRate(self):
        """Returns the value of consumptionRate"""
        return self.consumptionRate
    
    def setConsumptionRate(self, newConsumptionRate: int):
        """Sets the value of consumptionRate, ensuring it is in the range 0-150"""
        if newConsumptionRate >= 0 and newConsumptionRate <= 150:
            self.consumptionRate = newConsumptionRate

washModes = ["Daily wash", "Quick wash", "Eco"]

class SmartWashingMachine(SmartDevice):
    """SmartWashingMachine, inhertis from SmartDevice. Contains methods and properties that a smart washing machine may need to function"""
    def __init__(self):
        """Constructor, sets washMode to "Daily wash" by default"""
        super().__init__()
        self.washMode = "Daily wash"

    def __str__(self):
        """Returns a string containing information about the smart washing machine"""
        text = "Washing Machine - "
        text += "on, " if self.switchedOn else "off, "
        text += f"wash mode: {self.washMode}"
        return text
    
    def getWashMode(self):
        """Returns the value of washMode"""
        return self.washMode
    
    def setWashMode(self, newWashMode):
        """Sets the value of washMode, ensuring it is a valid wash mode, as specified in washModes"""
        if newWashMode in washModes:
            self.washMode = newWashMode

class SmartHome():
    """SmartHome, contains methods and properties that a smart home controller may need to function"""
    def __init__(self):
        """Constructor, sets devices to a new, empty array"""
        self.devices = []

    def __str__(self):
        """Returns a string containing information about all of the smart devices contained in the devices array"""
        text = "Smart Home - Devices:"
        for device in self.devices:
            text += "\n" + str(device)
        return text

    def getDevices(self):
        """Returns an array of devices in the smart home"""
        return self.devices
    
    def getDeviceAt(self, index: int):
        """Returns the device at the specified index in the array devices"""
        return self.devices[index]
    
    def addDevice(self, device: SmartDevice):
        """Appends a new device to the list of smart devices"""
        self.devices.append(device)

    def removeDevice(self, index: int):
        self.devices.pop(index)

    def toggleSwitch(self, index: int):
        """Toggles the switch of the device at the specified index in the list of smart devices"""
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        """Turns on all smart devices in the device list"""
        for device in self.devices:
            if not device.getSwitchedOn():
                device.toggleSwitch()
    
    def turnOffAll(self):
        """Turns off all smart devices in the device list"""
        for device in self.devices:
            if device.getSwitchedOn():
                device.toggleSwitch()

def testSmartPlug():
    """Tests the functionality of the SmartPlug class"""
    plug = SmartPlug()

    plug.toggleSwitch()
    print(plug.getSwitchedOn())
    print(plug.getConsumptionRate())
    plug.setConsumptionRate(60)
    print(plug.getConsumptionRate())
    print(plug)

def testSmartWashingMachine():
    """Tests the functionality of the SmartWashingMachine class"""
    washingMachine = SmartWashingMachine()

    washingMachine.toggleSwitch()
    print(washingMachine.getSwitchedOn())
    print(washingMachine.getWashMode())
    washingMachine.setWashMode("Eco")
    print(washingMachine.getWashMode())
    print(washingMachine)

def testSmartHome():
    """Tests the functionality of the SmartHome class"""
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

print("=== Backend Tests ===")
print("=== Smart Plug ===")
testSmartPlug()
print("=== Smart Washing Machine (Custom Device) ===")
testSmartWashingMachine()
print("=== Smart Home ===")
testSmartHome()