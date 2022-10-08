"""
reverses a string if its length is a multiple of 4.
"""

s=input("Enter The String: ")
S_len=len(s)
if S_len%4==0:
    print("Reverse String: ",s[::-1])
else:
    print("Not Reverse String: ",s)