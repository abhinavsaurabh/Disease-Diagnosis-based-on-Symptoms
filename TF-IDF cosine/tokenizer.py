
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



warnings.simplefilter("ignore")



# convert data to lower case


def convert_tolowercase(data):
    return data.lower()

# tokenizing using regextokenizer
def regextokenizer_func(data):
    tokenizer = RegexpTokenizer(r'\w+')
    data = tokenizer.tokenize(data)
    return data
