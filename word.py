import os, glob
import collections
import pandas as pd
import csv
from flask import Flask, render_template, request

app = Flask(__name__)
"""
Flask convention (__name__) is our variable is called 'app'. Creating an
instance & storing in a variable called 'app'
"""

path = "data/"
all_files = os.listdir(path)

# Word extraction from .csv files in data directory

for story in all_files:
   # open the file and then call .read() to get the text
   with open(os.path.join(path, story),"r") as f:
       
       text = f.read()

stopwords = set(line.strip() for line in open('data/stopwords.csv'))

wordcount = {}

for word in text.lower().split():
    word = word.replace("\h","")
    word = word.replace("\v","")
    word = word.replace("\s","")
    word = word.replace("-","")
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace(";","")
    word = word.replace("'","")
    word = word.replace("\"","")
    word = word.replace("\'","")
    word = word.replace("!","")
    word = word.replace("?","")
    word = word.replace("$","")
    word = word.replace("%","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print most common word

word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(10):
    print(word, ": ", count)
    

# Close the file
f.close()

# Count files in data directory
list = os.listdir('data/') # data/ is the directory path
number_files = len(list)
print(number_files, ": files in data directory")

# Pull name of csv files in data directory 
parent_dir = 'data/'
for csv_file in glob.glob(os.path.join(parent_dir, '*.csv')):
    print (csv_file)
