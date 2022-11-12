"""
Write a Python function to reverses a string if its length is a multiple of 4
"""
def str_reverse(str):
    Str_length=len(str)
    if Str_length%4==0:
        print("Reverse String: ",Str[: :-1])
    else:
        print("Not reverse String: ",Str)

Str=input("Enter the word: ")
str_reverse(Str)