"""
Write a Python function that takes a list of words and returns the length of the longest one
"""
def longest_Word(str):

    wordlist=s.split()
    List=[]
    for i in wordlist:
        List.append((len(i),i))
    List.sort()
    long_Word=List[-1][-1]
    long_word_length=List[-1][-2]
    return "The word with the longest is:",long_Word," and length is ",long_word_length

s=input("Enter the word: ")
print(longest_Word(s))
