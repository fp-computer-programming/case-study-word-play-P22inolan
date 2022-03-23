# Author: IBN (AMDG) 3/23/2022

def avoid(word, forbidden): # function for avoiding words
    for letter in word:
        if letter in forbidden:
            return False
    return True

string = input("Enter a string of forbidden letters: ") # input forbidden letters
string.islower()

counter = 0
print(string)
with open('/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words.txt') as infile:
    words = [] # list for words that don't contain forbidden letters
    for line in infile.readlines():
        if avoid(line, string):
            words.append(line.strip()) # appending to list

print(len(words))