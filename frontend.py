from backend import *;
from tkinter import *;

smartHome = SmartHome()
mainWin = Tk()
deviceTexts = []
turnedOnDevices = 0
lblCount = Label(mainWin, text=f"{turnedOnDevices} devices turned on")

def setupHome():
    """Creates and adds devices to the smartHome object"""
    smartHome.addDevice(SmartWashingMachine())
    smartHome.addDevice(SmartPlug())
    smartHome.addDevice(SmartWashingMachine())
    smartHome.addDevice(SmartPlug())
    smartHome.addDevice(SmartWashingMachine())

def setupWindow():
    """Sets the size, title and column sizes of the main window"""
    mainWin.geometry("550x78")
    mainWin.resizable(False, False)
    mainWin.title("Smart Home Controller - up2157117")
    mainWin.grid_columnconfigure(0, weight=2)
    mainWin.grid_columnconfigure(1, weight=1)
    mainWin.grid_columnconfigure(2, weight=1)
    mainWin.grid_columnconfigure(3, weight=1)

def resizeWindow(numOfDevices: int):
    mainWin.geometry(f"550x{78 + (26 * numOfDevices)}")

def configureDevice(device: SmartDevice):
    """Opens a new window containing configuration settings for a SmartDevice object"""
    configWin = Toplevel()
    configWin.geometry("250x50")
    configWin.resizable(False, False)
    configWin.title("Configure")
    configWin.grid_columnconfigure(0, weight=1)
    configWin.grid_columnconfigure(1, weight=1)

    entOption = Entry(configWin, width=15)
    entOption.grid(row=0, column=1, sticky="w")
    lblOption = Label(configWin, anchor="e", width=15)
    lblOption.grid(row=0, column=0, sticky="e")

    if isinstance(device, SmartPlug):
        entOption.insert(0, device.getConsumptionRate())
        lblOption.configure(text="Consumption Rate: ")
    elif isinstance(device, SmartWashingMachine):
        entOption.insert(0, device.getWashMode())
        lblOption.configure(text="Wash Mode: ")

    def submit():
        """Internal function to submit new values entered into the configuration window, into different attributes depending upon the class"""
        if isinstance(device, SmartPlug):
            device.setConsumptionRate(int(entOption.get()))
        elif isinstance(device, SmartWashingMachine):
            device.setWashMode(entOption.get())

        updateWidgets()
        configWin.destroy()

    btnCancel = Button(configWin, text="Cancel", command=configWin.destroy)
    btnCancel.grid(row=1, column=0)

    btnSubmit = Button(configWin, text="Submit", command=submit)
    btnSubmit.grid(row=1, column=1)

def updateWidgets():
    """Updates the list of devices shown in the main window"""
    turnedOnDevices = 0

    for i in range(0, len(deviceTexts)):
        deviceTexts[i].delete("1.0", END)
        deviceTexts[i].insert("1.0", str(smartHome.getDeviceAt(i)))
        if smartHome.getDeviceAt(i).getSwitchedOn():
            turnedOnDevices += 1

    lblCount.configure(text=f"{turnedOnDevices} devices turned on")

def setupWidgets():
    """Creates the widgets for all devices in the smartHome object"""
    def buttonTurnOn():
        """Internal function, turns all devices on and then updates the window"""
        smartHome.turnOnAll()
        updateWidgets()

    def buttonTurnOff():
        """Internal function, turns all devices off and then updates the window"""
        smartHome.turnOffAll()
        updateWidgets()

    btnAllOff = Button(mainWin, text="Turn all off", command=buttonTurnOff)
    btnAllOff.grid(row=1, column=0, padx=2, sticky="w")

    btnAllOn = Button(mainWin, text="Turn all on", command=buttonTurnOn)
    btnAllOn.grid(row=2, column=0, padx=2, sticky="w")

    numOfDevices = len(smartHome.getDevices())
    resizeWindow(numOfDevices)

    for i in range(0, numOfDevices):
        def toggleThis(index = i):
            """Internal function that toggles the device at index i in the array of SmartHome devices"""
            smartHome.toggleSwitch(index)
            updateWidgets()

        def configThis(index = i):
            """Internal function that opens a new configuration window for the device at index i"""
            configureDevice(smartHome.getDeviceAt(index))
            updateWidgets()

        txtDevice = Text(mainWin, height=1, width=50)
        txtDevice.insert("1.0", str(smartHome.getDeviceAt(i)))
        txtDevice.grid(row=(3 + i), column=0)

        deviceTexts.append(txtDevice)

        btnToggle = Button(mainWin, text="Toggle this", command=toggleThis)
        btnToggle.grid(row=(3 + i), column=1)

        btnConfig = Button(mainWin, text="Configure", command=configThis)
        btnConfig.grid(row=(3 + i), column=2)

    lblCount.grid(row=(4 + numOfDevices), column=0, padx=2, sticky="w")

def main():
    """Entry point for the application"""
    setupHome()
    setupWindow()
    setupWidgets()

    mainWin.mainloop()

main()