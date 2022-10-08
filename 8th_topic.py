"""
Write a Python program that will return true
if the two given integer values are equal or their sum or difference is 5
"""
a=int(input("Enter the A value: "))
b=int(input("Enter the B value: "))
print("Value is Equal: ",a is b)
if a+b==5:
    print("Value Sum:",a+b,"True")
elif a-b==5:
    print("Value Difference:",a-b,"True")
else:
    print("False")


#print("Value Sum:",a+b)
#print("Value Difference:",a-b)