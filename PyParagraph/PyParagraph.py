import os
import csv
import re

txtpath = input("Enter file path: ")
#txtpath = "paragraph_3.txt"

words = 0
sentences = 0
letters = 0
letterperword = 0
wordpersentence = 0

with open(txtpath, newline="") as txtfile:

    for row in txtfile:
        wordslist = row.split()
        words += len(wordslist)

        sentencelist = re.split("(?<=[.!?]) +", row)
        sentences += len(sentencelist)

    for word in wordslist:
        letters += len(word)

print("Paragraph Analysis")
print("---------------------------------------")
print(f"Approximate Word Count: {words}")
print(f"Approximate Sentence Count: {sentences}")
print(f"Average Letter Count: {round(letters/words,1)}") 
print(f"Average Sentence Length: {round(words/sentences,1)}")