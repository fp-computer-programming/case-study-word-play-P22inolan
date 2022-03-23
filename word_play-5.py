# Author: IBN (AMDG) 3/23/2022

def is_abecedarian(word): # function for words in alphabetical
    i = 0
    while i < len(word) - 1: 
        if word[i + 1] < word[i]: # if the letter after i + 1 is greater than i+1, reutrn False
            return False
        i += 1
    return True

with open('/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words.txt') as infile:
    words = [] # list for abecedarian words
    for line in infile.readlines():
        if is_abecedarian(line.strip()): # calling function
            words.append(line.strip()) # appending words to list

print(len(words)) # printing total amt