#Write a Python program to get the Factorial number of given number.
#Multiplication/Factorial
# 1st Method...
import math as mymath
n = int(input("Enter the value: "))
print(mymath.factorial(n))

#2nd Method....
#1*2*3*4*5*6......
In = int(input("Enter the Value: "))
Multi=1
for i in range(1,int(In+1)):
    Multi=Multi*i
    In=In-1
print("Factorial Value: ",Multi)
