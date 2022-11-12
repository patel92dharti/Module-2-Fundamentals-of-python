"""
Write a Python program to sum of three given integers.
However, if two values are equal sum will be zero
"""
a = int(input("Please enter A value: "))
b = int(input("Please enter B value: "))
c = int(input("Please enter C value: "))
if a==b:
    print("Total Value Sum is:",a-b)
elif b==c:
    print("Total Value Sum is:",b-c)
elif a==c:
    print("Total Value Sum is:",a-c)
else:
    print("Total Value Sum is:",a+b+c)
