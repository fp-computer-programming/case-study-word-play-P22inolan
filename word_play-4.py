# Author: INB (AMDG) 3/23/2022

def uses_only(word, available): # function for available letters
    for letter in word:
        if letter not in available:
            return False
    return True

string = input("Enter a string of allowed letters: ") # input string

with open('/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words.txt') as infile:
    words = [] # list for words with available letters
    for line in infile.readlines():
        if uses_only(line.strip(), string): # calling function
            words.append(line.strip()) # appending to list

print(len(words)) # printing total amt of words