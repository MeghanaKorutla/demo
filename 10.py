# Aim: To calculate distance using functions
# arguments with return type
# Author: Meghana
# Date: 28-02-23
def dist(u,a,t):
    s=u*t+0.5*a*t*t
    return s
x=int(input("enter the u value"))
y=int(input("enter a value"))
z=int(input("enter t value"))
result=dist(x,y,z)
print("distance is",result)
