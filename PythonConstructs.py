# This is a sequence i.e. a collcetion of characters
aString = "This is a sequence of characters"

# This is a condition
numberOfFlights = 10

if (numberOfFlights > 10):
    print("Number of flights greater than 10.")
else:
    print("Number of flights less than or equal to 10.")

# This is a for loop
airport = "Gatwick"

for char in airport:
    print(char)

# This is a while look
numberOfPlanesWaitingToTakeOff = 5

while(numberOfPlanesWaitingToTakeOff > 0):
    print("Plane taken off")
    numberOfPlanesWaitingToTakeOff = numberOfPlanesWaitingToTakeOff - 1

# This is a function
def StartEngine():
    print("Engine started.")

StartEngine()