import nltk.corpus
import re
import nltk
import time
from nltk.corpus import stopwords
import Stemmer
# from nltk.stem.snowball import SnowballStemmer
from config import *
# snow_stemmer = SnowballStemmer(language='english')

stemmer = Stemmer.Stemmer('english')
stop_words = stopwords.words('english')

def ck(a,stopword):
    if isinstance(a, int) and len(a)<4:
        return False
    elif len(a)<3:
        return False
    if a.isidentifier() and re.search(r"^M{0,3}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3})$",a):
        return True
    return True

def re_tok(a):
    tok_low = re.split(r'[^A-Za-z0-9]+', a)
    return tok_low

def re_tok_link(a):
    tok_low = re.split(r'[^A-Za-z0-9-/-:-.]+', a)
    return tok_low


def all_magic_happens_here(a,tag,st=True):
    # if tag=="extlink":
    #     gg=re_tok_link(a)
    # else:
    gg=re_tok(a)
    return_val=[]
    if st==False:
        for c in gg:
            if c!='':
                return_val.append(c)
        return return_val
    for g in gg:
        c=stemmer.stemWord(g)
        # c=snow_stemmer.stem(g) 
        if (c not in stop_words)and(c!=''):
            return_val.append(c)
    return return_val
