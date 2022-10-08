"""
get a single string from two given strings,
separated by a space and swap the first two characters of each string
"""

string1=input("Enter The Your First Name: ")
Stirng2=input("Enter the Your last Name: ")
New_st2=string1[:2] + Stirng2[2:]
New_st1=Stirng2[:2] +string1[2:]
sumString=New_st1+" "+New_st2
print("New Swap Characters String: ",sumString)