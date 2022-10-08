"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead
if the string length of the given string is less than 3,
leave it unchanged.
"""
s=input("Enter the your Company Name: ")
wordlist=s.split()
String_length=len(wordlist)
if String_length>=3:
    if s.endswith("ing"):
        print(s.__add__("ly"))
    else:
        print(s.__add__("ing"))
else:
    print(s)




