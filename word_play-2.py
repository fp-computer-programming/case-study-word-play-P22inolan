# Author: IBN (AMDG) 3/16/2022

wordfile = open("/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words.txt", "r")
without = open("/Users/p22inolan/Desktop/case studies/case-study-word-play-P22inolan/words_without_e.txt", "a")

def no_e(words):
    totalcount = 0
    nocount = 0
    while True:
        line = words.readline()
        if "e" not in line:
            without.write(line)
            totalcount += 1
        elif "e" in line:
            nocount += 1
            totalcount += 1
        if len(line) == 0:
            break
    percentage = (nocount/totalcount) * 100
    return "{0} percent of the words do not contain e.".format(percentage)


print(no_e(wordfile))
wordfile.close()
without.close()
