#Write a Python program to get the Fibonacci series of given range.
"""..............Fibonacci series..............
0,1,1,2,3,5,8,13,21,34,55,89,144.................
"""
n=int(input("Enter the Value: "))
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b

