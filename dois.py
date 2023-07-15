import csv
import pandas as pd
import os
import json
from itertools import groupby



# fetch dois from scite csv file and append them to a list, contains monist and mind papers
def grabdois():
    column_names = ["journal","doi","title","pmid","authors","issns","supporting_cites","contrasting_cites","mentioning_cites","total_cites","scite_report_link"]
    df = pd.read_csv("scitedata.csv",names = column_names)
    dois = df.doi.to_list()

    # remove header from list
    dois.remove(dois[0])
    return dois


# reads all forward citation files for each doi specified in grabdois function
path = '/Users/markhorner/Desktop/github/cent19/doidata'
os.chdir(path)
stored = {}

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        # doc = f.read()
        lines = [line.rstrip('\n') for line in f]
        global lists
        lists = [[]]
        for i in lines:
            if len(i) > 0:
                lists[-1].append(i)
            else:
                lists.append([])
            


# iterate through all file
def extract():
    for file in os.listdir():
    # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
        # call read text file function
            read_text_file(file_path)
    return lists[1]

print(extract())



