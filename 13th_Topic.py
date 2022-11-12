#Write a Python program to count the occurrences of each word in a given sentence
def word_count(str):
    count=dict()
    words=str.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count

print(word_count("the quick brown fox jumps over the lazy dog."))
