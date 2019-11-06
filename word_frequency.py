# Slow version:

import re

#-------------------------------------------------------------

file_name = r"C:\Users\Witek\Desktop\pan-tadeusz.txt"

text = open(file_name, encoding="utf8").read()
words = text.replace("\n", " ")
words = re.sub('[^A-Za-z0-9ąćęłńóśźż]+', ' ', words)
words = words.split(' ')
words.sort()

#-------------------------------------------------------------

wor = []

def word_find(word, words):
    count = 0

    for x, x_word in enumerate(words):
        if word == x_word:
            count +=1

        if x == words.__len__()-1:
            return count

    return False

#-------------------------------------------------------------

def word_frequency(words_len, count):
    word_f = count/words_len

    return word_f

#-------------------------------------------------------------

f_save = open("counted_words.txt","w")

for x, word in enumerate(words):
    count = word_find(word, words)
    freq = word_frequency(words.__len__(), count)

    if count > 1:
        del words[x+1:x+count]

    wor.append([[word], [count], [freq]])

    f_save.write(word+" "+str(count)+" "+str(freq)+"\n")

    count = 0
    freq = 0

print(wor)
