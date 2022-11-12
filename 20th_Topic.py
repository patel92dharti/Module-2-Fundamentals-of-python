#Write a Python function to insert a string in the middle of a string
Stirng = "Python is Good But Still Join the"
Mid_Word= input("Enter Mid Word: ")
Word_List=list(Mid_Word.split())
List=list(Stirng.split())
String_len=len(List)//2
s_T=List[0:String_len] + Word_List + List[String_len: :]
s_T=" ".join(s_T)
print("After Added Middle String:",s_T)

