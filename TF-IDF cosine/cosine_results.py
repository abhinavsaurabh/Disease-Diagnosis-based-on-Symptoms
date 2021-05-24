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

def cosine_sim_results(k,final_symp,M,columns_name,D,diseases,tf,idf):
  topk2=cosine_similarity(k,final_symp,M,columns_name,D,tf,idf)
  print(f"Top {k} disease based on Cosine Similarity Matching :\n ")
  topk2_sorted = dict(sorted(topk2.items(), key=lambda kv: kv[1], reverse=True))
  j = 0
  topk2_index_mapping = {}
  for key in topk2_sorted:
      print(f"{j}. Disease : {diseases[key]} \t Score : {round(topk2_sorted[key], 2)}")
      topk2_index_mapping[j] = diseases[key]
      j += 1


  select = input("\nMore details about the disease? Enter index of disease or '-1' to discontinue and close the system:\n")
  if select!='-1':
      dis=topk2_index_mapping[int(select)]
      print()
      print(diseaseDetail(dis))


# function for cosine dot product
def cosine_dot(a, b):
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0
    else:
        temp = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        return temp


# function to calculte Cosine Similarity
def cosine_similarity(k, query,M,columns_name,D,tf,idf):
    d_cosines = []
    query_vector = gen_vector(query,M,columns_name,tf,idf)
    for d in D:
        d_cosines.append(cosine_dot(query_vector, d))
    out = np.array(d_cosines).argsort()[-k:][::-1]

    final_display_disease={}
    for lt in set(out):
        final_display_disease[lt] = float(d_cosines[lt])
    return final_display_disease


def gen_vector(tokens,M,columns_name,tf,idf):
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
