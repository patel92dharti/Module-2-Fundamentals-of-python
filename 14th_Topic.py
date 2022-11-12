"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string
"""

Str1=input("Enter the first name: ")
Str2=input("Enter the Last Name: ")
print("Without Swap Single String: ",Str1+" "+Str2)
NewSt1=Str2[:2] + Str1[2:]
NewSt2=Str1[:2] + Str2[2:]
print("With Swap Single String: ",NewSt1+" "+NewSt2)