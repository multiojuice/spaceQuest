import math
import sys
proceed = input("Welcome to Tsiolkovsky rocket equation, input Anything to continue: ")

print("The Tsiolkovsky rocket equation is represented as")
print("DeltaV=Ve*ln*(Mo/Mf)")
V = int(input("Input your value for effective exhaust velocity: "))
O = int(input("Input your value for initial total mass: "))
while (O <= 0):
    O = int(input("Input a valid value for your value for initial total mass: "))
F= int(input("Input your value for final total mass: "))
while (F <= 0):
    F = int(input("Input a valid value for your value for final total mass: "))
   
answer = (V*(math.log(O/F)))
print("Your maximum change in velocity is",answer)
    
          


