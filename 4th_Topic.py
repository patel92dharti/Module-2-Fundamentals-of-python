#swap two number with temp variable and without temp variable

A,B=20,50
Temp_var1,Temp_var2=A,B
print("Old Value Of A: ",A,"Temp1 Variable Value: ",A)
print("Old Value Of B: ",B,"Temp2 Variable Value: ",B)
A=A ^ B
B=B ^ A
A=A ^ B
print("Swap Value Of A: ",A,"Temp1 Variable Swap Value: ",A)
print("Swap Value Of B: ",B,"Temp1 Variable Swap Value: ",B)

import sys
print(sys.copyright)
