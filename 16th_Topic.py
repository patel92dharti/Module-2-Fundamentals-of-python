"""
first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor',
replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
"""
String= "Life is never fair and perhaps it is a poor thing for most of us that it is not " \
        "Don't be afraid to give up the poor to go for the great."
snot =String.find("not")
spoor=String.find("poor")
if snot>0 and spoor>0:
    String=String.replace("not","good")
    if snot>0 and spoor>0:
        String = String.replace("poor", "good")
        print("New String: ",String)
else:
    print("Old String: ",String)
