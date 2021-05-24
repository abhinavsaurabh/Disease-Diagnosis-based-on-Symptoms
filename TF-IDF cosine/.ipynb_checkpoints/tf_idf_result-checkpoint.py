from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from statistics import mean
from nltk.corpus import wordnet
import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split,cross_val_score
import math
from bs4 import BeautifulSoup
from itertools import combinations
from time import time
from collections import Counter
import operator
import warnings
import operator
import pickle
import numpy as np
import requests
import re
from googlesearch import search

# function to generate query vector for tf_idf
def gen_vector(tokens):
    Q = np.zeros(M)
    counter = Counter(tokens)
    query_weights = {}
    for token in np.unique(tokens):
        tf = counter[token]
        try:
            idf_temp=idf[token]
        except:
            pass
        try:
            ind = columns_name.index(token)
            Q[ind] = tf*idf_temp
        except:
            pass
    return Q


# function to calculate tf_idf_score
def tf_idf_score(k, query,tf_idf):
    query_weights = {}
    for key in tf_idf:
        if key[1] in query:
            try:
                query_weights[key[0]] += tf_idf[key]
            except:
                query_weights[key[0]] = tf_idf[key]
    query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)

    l = []
    for i in query_weights[:k]:
        l.append(i)
    return l

def tf_idf_results(k,final_symp,tf_idf):
    topk1=tf_idf_score(k,final_symp,tf_idf)
    print(f"\nTop {k} diseases predicted based on TF_IDF Matching :\n")
    i = 0
    topk1_index_mapping = {}
    for key, score in topk1:
        print(f"{i}. Disease : {key} \t Score : {round(score, 2)}")
        topk1_index_mapping[i] = key
        i += 1

    select = input("\nMore details about the disease? Enter index of disease or '-1' to discontinue:\n")
    if select!='-1':
        dis=topk1_index_mapping[int(select)]
        print()
        print(diseaseDetail(dis))


def diseaseDetail(term):
    diseases=[term]
    ret=term+"\n"
    for dis in diseases:
        # search "disease wilipedia" on google
        query = dis+' wikipedia'
        for sr in search(query,tld="co.in",stop=10,pause=0.5):
            # open wikipedia link
            match=re.search(r'wikipedia',sr)
            filled = 0
            if match:
                wiki = requests.get(sr,verify=False)
                soup = BeautifulSoup(wiki.content, 'html5lib')
                # Fetch HTML code for 'infobox'
                info_table = soup.find("table", {"class":"infobox"})
                if info_table is not None:
                    # Preprocess contents of infobox
                    for row in info_table.find_all("tr"):
                        data=row.find("th",{"scope":"row"})
                        if data is not None:
                            symptom=str(row.find("td"))
                            symptom = symptom.replace('.','')
                            symptom = symptom.replace(';',',')
                            symptom = symptom.replace('<b>','<b> \n')
                            symptom=re.sub(r'<a.*?>','',symptom) # Remove hyperlink
                            symptom=re.sub(r'</a>','',symptom) # Remove hyperlink
                            symptom=re.sub(r'<[^<]+?>',' ',symptom) # All the tags
                            symptom=re.sub(r'\[.*\]','',symptom) # Remove citation text
                            symptom=symptom.replace("&gt",">")
                            ret+=data.get_text()+" - "+symptom+"\n"
#                            print(data.get_text(),"-",symptom)
                            filled = 1
                if filled:
                    break
    return ret
