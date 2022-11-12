"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor',
replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
"""
def find_string(str):
    Stnot=str.find("not")
    Stpoor=str.find("poor")
    if Stpoor>Stnot and Stnot>0 and Stpoor>0:
        str=str.replace(str[Stnot:(Stpoor+4)],"Good")
        return str
    else:
        return str

String= "The lyrics is not that ha poor!"

print(find_string(String))
