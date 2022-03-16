# Author: IBN (AMDG) 3/16/2022

wordfile = open("/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words.txt", "r")
without = open("/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words_without_e.txt", "a")

def no_e(words):
    while True:
        totalcount = 0
        nocount = 0
        line = words.readline()
        if "e" not in line:
            without.write(line)
            totalcount += 1
        elif "e" in line:
            nocount += 1
            totalcount += 1
        elif len(line) == 0:
            print("{0} % of the words contain the letter e.".format((nocount/totalcount) * 100))
            break

print(no_e(wordfile))