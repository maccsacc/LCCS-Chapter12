import random
#thermostat
def thermostatModel(actual, target):
    if actualTemp < targetTemp:
        return 1
    else:
        return 0
    
targetTemp = int(input("Input your target temperature: "))
for i in range(100):
    actualTemp = random.randint(10,30)
    tempOnorOff = thermostatModel(actualTemp,targetTemp)
    print("Actual: " + str(actualTemp) + ", Target: " + str(targetTemp) + ", Heater: " + str(tempOnorOff))

