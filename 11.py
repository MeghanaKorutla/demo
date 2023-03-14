# Aim: To calculate sum,diff,product & quotient of two numbers using functions
# arguments with return type
# Author: Meghana
# Date: 28-02-23
def fun(a,b):
    s=a+b
    d=a-b
    p=a*b
    q=a%b
    return s,d,p,a
x=int(input("enter first num"))
y=int(input("enter second number"))
m,n,o,r=fun(x,y)
print("sum is",m)
print("diff is",n)
print("product is",o)
print("quotient is",r)
