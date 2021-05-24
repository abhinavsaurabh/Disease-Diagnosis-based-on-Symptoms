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


def syno(term):
    splitter = RegexpTokenizer(r'\w+')
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    syno = []
    resthesaurus = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(resthesaurus.content,  "html.parser")
    try:
        container=soup.find('section', {'class': 'MainContentContainer'})
        row=container.find('div',{'class':'css-191l5o0-ClassicContentCard'})
        row = row.find_all('li')
        for x in row:
            syno.append(x.get_text())
    except:
        None
    for syn in wordnet.synsets(term):
        syno+=syn.lemma_names()
    return set(syno)

def generatesymptoms2(processed_user_symptoms):

    user_symptoms = []
    for user_sym in processed_user_symptoms:
        user_sym = user_sym.split()
        str_sym = set()
        for comb in range(1, len(user_sym)+1):
            for subset in combinations(user_sym, comb):
                subset=' '.join(subset)
                subset = syno(subset)
                str_sym.update(subset)
        str_sym.add(' '.join(user_sym))
        user_symptoms.append(' '.join(str_sym).replace('_',' '))
    # query expansion performed by joining synonyms found for each symptoms initially entered
    print("After query expansion done by using the symptoms entered")
    print(user_symptoms)

    return user_symptoms
