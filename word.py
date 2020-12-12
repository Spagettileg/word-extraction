import os
import collections
import pandas as pd

path = "data/"
all_files = os.listdir(path)

for story in all_files:
   # open the file and then call .read() to get the text
   with open(os.path.join(path, story),"rt") as f:

        text = f.read()

stopwords = set(line.strip() for line in open('data/stopwords.csv'))

wordcount = {}

for word in text.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace(";","")
    word = word.replace("'","")
    word = word.replace("/","")
    word = word.replace("\"","")
    word = word.replace("\'","")
    word = word.replace("!","")
    word = word.replace("?","")
    word = word.replace("-","")
    word = word.replace("--","")
    word = word.replace("$","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)

# Close the file
f.close()


# Count files in data directory
list = os.listdir('data/') # data/ is your directory path
number_files = len(list)
print(number_files, ": files in data directory")