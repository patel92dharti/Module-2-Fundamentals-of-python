#Write a python program to sum of the first n positive integers.
#1+2+3+ =6
n =int(input("Enter the value:"))
SUM= 0
for i in range(1,n+1):
    SUM=SUM+i
print("SUM: ",SUM)
