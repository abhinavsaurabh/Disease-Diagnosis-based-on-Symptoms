import warnings
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split, cross_val_score
from statistics import mean
from nltk.corpus import wordnet
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from itertools import combinations
from time import time
from collections import Counter
import operator
from xgboost import XGBClassifier
import math
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.neural_network import MLPClassifier as mlp
import re
from googlesearch import search
import warnings
warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup


def mlp1(X,Y,sample_x,df_norm,dataset_symptoms,final_symp,scores):
  obj=mlp(hidden_layer_sizes=(200,50),max_iter=1000,solver='adam')
  obj.fit(X,Y)
  prediction = obj.predict_proba([sample_x])

  k = 10
  diseases = list(set(Y['label_dis']))
  diseases.sort()
  topk = prediction[0].argsort()[-k:][::-1]

  print(f"\nTop {k} diseases predicted based on symptoms by MLP")
  topk_dict = {}
  # Show top 10 highly probable disease to the user.
  for idx,t in  enumerate(topk):
      match_sym=set()
      row = df_norm.loc[df_norm['label_dis'] == diseases[t]].values.tolist()
      row[0].pop(0)

      for idx,val in enumerate(row[0]):
          if val!=0:
              match_sym.add(dataset_symptoms[idx])
      prob = (len(match_sym.intersection(set(final_symp)))+1)/(len(set(final_symp))+1)
      prob *= mean(scores)
      topk_dict[t] = prob
  j = 0
  topk_index_mapping = {}
  topk_sorted = dict(sorted(topk_dict.items(), key=lambda kv: kv[1], reverse=True))
  for key in topk_sorted:
    prob = topk_sorted[key]*100
    print(str(j) + " Disease name:",diseases[key], "\tProbability:",str(round(prob, 2))+"%")
    topk_index_mapping[j] = key
    j += 1

  select = input("\nMore details about the disease? Enter index of disease or '-1' to discontinue and close the system:\n")
  if select!='-1':
      dis=diseases[topk_index_mapping[int(select)]]
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
                            filled = 1
                if filled:
                    break
    return ret
