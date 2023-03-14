# Aim: To calculate simple intrest using functions
# Use no arguments no return type
# Author: Meghana
# Date: 28-02-23
def si():
    p=int(input("enter the principle"))
    t=int(input("enter the time"))
    r=float(input("enter the rate of intrest"))
    si=(p*t*r)/100
    print("simple intrest is",si)
si()
