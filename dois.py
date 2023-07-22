import csv
import pandas as pd
import os
import json
from itertools import groupby

# the data format we want is a list of dictionarys
# [{'OCIT': original citation doi, 'TY': GENERIC, 'DO': 10.1215/9781478021872, ...,'ER': },
# {'OCIT': original citation doi, 'TY': GENERIC, 'DO': 10.1215/9781478021872, ...,'ER': }]

# define variables
citation_list = []
stored = {}

# fetch dois from scite csv file and append them to a list, contains monist and mind papers
def grabdois():
    column_names = ["journal","doi","title","pmid","authors","issns","supporting_cites","contrasting_cites","mentioning_cites","total_cites","scite_report_link"]
    df = pd.read_csv('scitedata.csv',names = column_names)
    dois = df.doi.tolist()

    # remove header from list
    dois.remove(dois[0])
    return dois


# reads all forward citation files for each doi specified in grabdois function
path = '/Users/markhorner/Desktop/github/cent19/doidata'
os.chdir(path)
k = 0
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(file)
        global lol
        lol = [[]]
        lines = [line.rstrip('\n') for line in f]
        for i in lines:
            if len(i) > 0:
                lol[-1].append(i)
            else:
                lol.append([])
        print(len(lol))
        global k
        if len(lol) == 1:
            citation_list.append({'ODOI':file})
            k += 1
        else:
            for citation in lol:
                citation_list.append({})
                citation_list[k]['ODOI'] = file
                for item in citation:
                    citation_list[k][item[:2]] = item[6:]
                k += 1

            


# iterate through all files and create dictionary with key-value pair that denotes ODOI and the file name
def extract():
    global file
    for file in os.listdir():
    # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            # append each forward citation extracted by read_text_file and insert each of those citations into the files corresponding dict entry in citation list

        # call read text file function
            read_text_file(file_path)
    return citation_list

bust = [1,2,3]

def writejson(path, data):
    path = '/Users/markhorner/Desktop/github/cent19/fwdcite.json'
    with open(path, 'w') as f:
        # for i in data:
        json.dump(data, f, indent = 2)



# [{'ODOI': '10.5840:monist18922321.txt'}, {'ODOI': '10.1093:monist:9.1.1.txt'}]
# Everything in the format function must be moved to the read_text_file function so that after each file is opened and
# its name(doi) is added to the citation list of dicts, we can add all that files forward citation data at the same time


writejson(path, extract())
# print(format())








    



