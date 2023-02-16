from backend import *;
from tkinter import *;

smartHome = SmartHome()
mainWin = Tk()
deviceTexts = []
turnedOnDevices = 0
lblCount = Label(mainWin, text=f"{turnedOnDevices} devices turned on")

def setupHome():
    smartHome.addDevice(SmartWashingMachine())
    smartHome.addDevice(SmartPlug())
    smartHome.addDevice(SmartWashingMachine())
    smartHome.addDevice(SmartPlug())
    smartHome.addDevice(SmartWashingMachine())

def setupWindow():
    mainWin.geometry("480x112")
    mainWin.resizable(False, False)
    mainWin.title("Smart Home Controller - up2157117")
    mainWin.grid_columnconfigure(0, weight=2)
    mainWin.grid_columnconfigure(1, weight=1)
    mainWin.grid_columnconfigure(2, weight=1)

def updateWidgets():
    turnedOnDevices = 0

    for i in range(0, len(deviceTexts)):
        deviceTexts[i].delete("1.0", END)
        deviceTexts[i].insert("1.0", str(smartHome.getDeviceAt(i)))
        if smartHome.getDeviceAt(i).getSwitchedOn():
            turnedOnDevices += 1

    lblCount.configure(text=f"{turnedOnDevices} devices turned on")

def setupWidgets():
    lblTitle = Label(mainWin, text="Smart Home", font=("Segoe UI", 18))
    lblTitle.grid(row=0, column=0, columnspan=2)

    def buttonTurnOn():
        smartHome.turnOnAll()
        updateWidgets()

    def buttonTurnOff():
        smartHome.turnOffAll()
        updateWidgets()

    btnAllOff = Button(mainWin, text="Turn all off", command=buttonTurnOff)
    btnAllOff.grid(row=1, column=0, padx=2, sticky="w")

    btnAllOn = Button(mainWin, text="Turn all on", command=buttonTurnOn)
    btnAllOn.grid(row=2, column=0, padx=2, sticky="w")

    numOfDevices = len(smartHome.getDevices())
    mainWin.geometry(f"480x{112 + (26 * numOfDevices)}")

    for i in range(0, numOfDevices):
        def toggleThis(index=i):
            smartHome.toggleSwitch(index)
            updateWidgets()

        txtDevice = Text(mainWin, height=1, width=50)
        txtDevice.insert("1.0", str(smartHome.getDeviceAt(i)))
        txtDevice.grid(row=(3 + i), column=0)

        deviceTexts.append(txtDevice)

        btnToggle = Button(mainWin, text="Toggle this", command=toggleThis)
        btnToggle.grid(row=(3 + i), column=1)

    lblCount.grid(row=(4 + numOfDevices), column=0, padx=2, sticky="w")

def main():
    setupHome()
    setupWindow()
    setupWidgets()

    mainWin.mainloop()

main()