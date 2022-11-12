"""
Write a Python program that will return true
if the two given integer values are equal or their sum or difference is 5
"""
def difference(a,b):
    if a==b or abs(a-b)==5 or (a+b)==5:
        return True
    else:
        return False
a=int(input("Enter the Value: "))
b=int(input("Enter the Value: "))
print(difference(a,b))
