# Author: IBN (AMDG) 3/16/2022

words = open("/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words.txt", "r")
greater = open("greater_than_20.txt", "a")
while True: # starting while loop for reading the file
    line = words.readline()
    if len(line) > 20: # finding words over 20
        greater.write(line)
    elif len(line) == 0: # Breaking once end is reached
        break
greater.close()
words.close()

