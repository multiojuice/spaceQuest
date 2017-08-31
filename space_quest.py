import math
import sys
def getRocketNumber(stringInput,bot,top):
    while True:
        try:
            num = int(input("Enter your value for " + stringInput))
            break
        except ValueError:
            print("Please enter a number...")
    while bot> num or num > top:
        num = int(input("Please enter a legitament value for " + stringInput))
    return num
print("The Tsiolkovsky rocket equation is represented as")
print("DeltaV=Ve*ln*(Mo/Mf)")
V = getRocketNumber("Effective Exhaust Velocity: ", 400, 5000)
O = getRocketNumber("Initial Mass: ", 0, 1000000000)
F = getRocketNumber("Final Mass: ",0 ,1000000000)
answer = (V*(math.log(O/F)))
print("Your maximum change in Velocity is", answer)
    
          


