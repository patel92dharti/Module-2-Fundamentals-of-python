"""
get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
"""
String=input("Enter the String: ")
S_len=len(String)
S_Total=String[0:2] + String[-2:]
if S_len<=2:
    print(" ")
else:
    print(S_Total)
