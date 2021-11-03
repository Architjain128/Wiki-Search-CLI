import nltk.corpus
import re
import nltk
import time
import Stemmer
from config import *

stemmer = Stemmer.Stemmer('english')
stop_words=['myself', 'ours', 'ourselves', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'himself', "she's", 'hers', 'herself', "it's", 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'whom', 'this', 'that', "that'll", 'these', 'those', 'were', 'been', 'being', 'have', 'having', 'does', 'doing', 'because', 'until', 'while', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'down', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'both', 'each', 'more', 'most', 'other', 'some', 'such', 'only', 'same', 'than', 'very', 'will', 'just', "don't", 'should', "should've", 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", "isn't", 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", "won't", 'wouldn', "wouldn't"]


def re_tok(a):
    tok_low = re.split(r'[^A-Za-z0-9]+', a)
    return tok_low,len(tok_low)

def re_tok_link(a):
    tok_low = re.split(r'[^A-Za-z0-9-/-:-.]+', a)
    return tok_low

def stemm(a):
    without_stop=[]
    for word in a:
        word = stemmer.stemWord(word) 
        if word in stop_words:
            continue
        without_stop.append(word)
    return without_stop

def all_magic_happens_here(a,tag,st=True):
    # if tag=="extlink":
    #     gg=re_tok_link(a)
    # else:
    gg,vv=re_tok(a)
    gg=list(set(gg))
    return_val=[]
    return_val1=[]
    if st==False:
        for c in gg:
            if c!='':
                return_val1.append(c)
        return return_val,vv
    
    for g in gg:
        c=stemmer.stemWord(g)
        # c=snow_stemmer.stem(g) 
        if (c not in stop_words)and(c!=''):
            return_val.append(c)
    return return_val,vv
