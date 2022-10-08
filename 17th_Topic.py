"""
takes a list of words and returns the length of the longest one.
"""
s=input("Enter the word: ")
wordlist=s.split()
List=[]
for i in wordlist:
    List.append((len(i),i))
List.sort()
print("The word with the longest is:",List[-1][-1]," and length is ",len(List[-1][-1]))

