from backend import *;
from tkinter import *;

smartHome = SmartHome()
mainWin = Tk()
deviceWidgets = []
lblCount = Label(mainWin, text=f"{smartHome.getTurnedOnDevices()} devices turned on")
btnAddDevice = Button(mainWin, text="Add Device")

def setupHome():
    """Creates and adds devices to the smartHome object"""
    smartHome.addDevice(SmartWashingMachine())
    smartHome.addDevice(SmartPlug())
    smartHome.addDevice(SmartWashingMachine())
    smartHome.addDevice(SmartPlug())
    smartHome.addDevice(SmartWashingMachine())

def setupWindow():
    """Sets the title and column sizes of the main window"""
    mainWin.resizable(False, False)
    mainWin.title("Smart Home Controller - up2157117")
    mainWin.grid_columnconfigure(0, weight=2)
    mainWin.grid_columnconfigure(1, weight=1)
    mainWin.grid_columnconfigure(2, weight=1)
    mainWin.grid_columnconfigure(3, weight=1)

def resizeWindow():
    """Resizes the main window to fit new devices, and moves lblCount and btnAddDevice to the bottom-most row"""
    mainWin.geometry(f"600x{78 + (26 * len(smartHome.getDevices()))}")
    lblCount.grid(row=100, column=0, padx=2, sticky="w")
    btnAddDevice.grid(row=100, column=3)

def addDevice():
    """Opens a new window for user input to add a new device to the SmartHome object"""
    addDeviceWin = Toplevel()
    addDeviceWin.geometry("300x57")
    addDeviceWin.resizable(False, False)
    addDeviceWin.title("Add New Device")
    addDeviceWin.grid_columnconfigure(0, weight=1)
    addDeviceWin.grid_columnconfigure(1, weight=1)

    deviceOptions = ["Smart Plug", "Smart Washing Machine"]

    selected = StringVar()
    selected.set("Smart Plug")

    optDeviceType = OptionMenu(addDeviceWin, selected, *deviceOptions)
    optDeviceType.grid(row=0, column=0, columnspan=2)

    def submit():
        if selected.get() == "Smart Plug":
            smartHome.addDevice(SmartPlug())
        elif selected.get() == "Smart Washing Machine":
            smartHome.addDevice(SmartWashingMachine())

        setupDeviceWidgets(len(smartHome.getDevices()) - 1)
        resizeWindow()
        addDeviceWin.destroy()

    btnCancel = Button(addDeviceWin, text="Cancel", command=addDeviceWin.destroy)
    btnCancel.grid(row=1, column=0)

    btnSubmit = Button(addDeviceWin, text="Submit", command=submit)
    btnSubmit.grid(row=1, column=1)

def removeDevice(index):
    """Removes the device at the specified index from both the interface, and the smartHome object"""
    for widget in deviceWidgets[index]:
        widget.grid_remove()

    smartHome.removeDevice(index)
    deviceWidgets.pop(index)

    for i in range(0, len(deviceWidgets)):
        deviceWidgets[i][3].configure(command=lambda index=i : removeDevice(index))
        for j in range(0, len(deviceWidgets[i])):
            deviceWidgets[i][j].grid(row=(2 + i))

    resizeWindow()
    updateWidgets()

def setupDeviceWidgets(index: int):
    """Add the widgets necessary for each device, given their index in the list of smartHome's devices"""
    def toggleThis():
        smartHome.toggleSwitch(index)
        updateWidgets()

    def configThis():
        configureDevice(smartHome.getDeviceAt(index))
        updateWidgets()

    txtDevice = Text(mainWin, height=1, width=50)
    txtDevice.insert("1.0", str(smartHome.getDeviceAt(index)))
    txtDevice.grid(row=(2 + index), column=0)

    btnToggle = Button(mainWin, text="Toggle this", command=toggleThis)
    btnToggle.grid(row=(2 + index), column=1)

    btnConfig = Button(mainWin, text="Configure", command=configThis)
    btnConfig.grid(row=(2 + index), column=2)

    btnDelete = Button(mainWin, text="Remove", command=lambda i=index : removeDevice(i))
    btnDelete.grid(row=(2 + index), column=3)

    widgets = [txtDevice, btnToggle, btnConfig, btnDelete]
    deviceWidgets.append(widgets)

def configureDevice(device: SmartDevice):
    """Opens a new window containing configuration settings for a SmartDevice object"""
    configWin = Toplevel()
    configWin.geometry("250x68")
    configWin.resizable(False, False)
    configWin.title("Configure")
    configWin.grid_columnconfigure(0, weight=1)
    configWin.grid_columnconfigure(1, weight=1)

    entOption = Entry(configWin, width=15)
    entOption.grid(row=0, column=1, sticky="w")
    lblOption = Label(configWin, anchor="e", width=15)
    lblOption.grid(row=0, column=0, sticky="e")
    lblValidOptions = Label(configWin)
    lblValidOptions.grid(row=1, column=0, columnspan=2)

    if isinstance(device, SmartPlug):
        entOption.insert(0, device.getConsumptionRate())
        lblOption.configure(text="Consumption Rate: ")
        lblValidOptions.configure(text="(Any integer, 0-150)")
    elif isinstance(device, SmartWashingMachine):
        entOption.insert(0, device.getWashMode())
        lblOption.configure(text="Wash Mode: ")
        lblValidOptions.configure(text="(Daily wash, Quick wash or Eco)")

    def submit():
        if isinstance(device, SmartPlug):
            device.setConsumptionRate(int(entOption.get()))
        elif isinstance(device, SmartWashingMachine):
            device.setWashMode(entOption.get())

        updateWidgets()
        configWin.destroy()

    btnCancel = Button(configWin, text="Cancel", command=configWin.destroy)
    btnCancel.grid(row=2, column=0)

    btnSubmit = Button(configWin, text="Submit", command=submit)
    btnSubmit.grid(row=2, column=1)

def updateWidgets():
    """Updates the list of devices shown in the main window"""
    for i in range(0, len(deviceWidgets)):
        # Remove and replace the text of the label for each device
        deviceWidgets[i][0].delete("1.0", END)
        deviceWidgets[i][0].insert("1.0", str(smartHome.getDeviceAt(i)))

    lblCount.configure(text=f"{smartHome.getTurnedOnDevices()} devices turned on")

def setupWidgets():
    """Creates the widgets for all devices in the smartHome object"""
    def buttonTurnOn():
        smartHome.turnOnAll()
        updateWidgets()

    def buttonTurnOff():
        smartHome.turnOffAll()
        updateWidgets()

    btnAllOff = Button(mainWin, text="Turn all off", command=buttonTurnOff)
    btnAllOff.grid(row=0, column=0, padx=2, sticky="w")

    btnAllOn = Button(mainWin, text="Turn all on", command=buttonTurnOn)
    btnAllOn.grid(row=1, column=0, padx=2, sticky="w")

    for i in range(0, len(smartHome.getDevices())):
        setupDeviceWidgets(i)

    btnAddDevice.configure(command=addDevice)

    resizeWindow()

def main():
    """Entry point for the application"""
    setupHome()
    setupWindow()
    setupWidgets()

    mainWin.mainloop()

main()