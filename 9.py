# Aim: To print sum of five numbers using functions
# arguments without return type
# Author: Meghana
# Date: 28-02-23
def add(a,b,c,d,e):
    s=a+b+c+d+e
    return s
x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))
w=int(input("enter the fourth number"))
t=int(input("enter the fifth number"))
result=add(x,y,z,w,t)
print("sum=",result)
