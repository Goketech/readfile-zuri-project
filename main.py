# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from typing import TextIO


def read_file_content(filename):
    # [assignment] Add your code here
    with open('C:/Users/USER/Desktop/Reading-Text-Files/Reading-Text-Files/story.txt', 'r') as f:
        b = f.read()
        return b

def count_words():
    text = read_file_content("C:/Users/USER/Desktop/Reading-Text-Files/Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    s = text.split()
    #print(s)
    count = {}
    for word in s:
        if word in count:
            count[word] += 1
        else:
            count[word] =1
    return count

print(count_words())