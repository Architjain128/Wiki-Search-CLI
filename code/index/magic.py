import re
import nltk
import time
try:
    from nltk.corpus import stopwords
finally:
    nltk.download('stopwords')
    from nltk.corpus import stopwords
try:
    from nltk.stem import WordNetLemmatizer
finally:
    nltk.download('wordnet')
    from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer

# pageCount=int(52622)

def all_magic_happens_here(a,tag,fl=2):
    list_of_all_lowecase_words = re_tok_lower(a,tag)
    set_non_stop_words=rem_stop_words(list_of_all_lowecase_words)
    if fl==0:
        lemmy_words=lemm(set_non_stop_words,tag)
    if fl ==1:
        stemmy_words=porter_stemm(set_non_stop_words,tag)
    if fl ==2:
        stemmy_words=snow_stemm(set_non_stop_words,tag)
    return list_of_all_lowecase_words


def re_tok_lower(a,tag):
    tok_low = re.split(r'[^A-Za-z0-9]+', a.strip().lower())
    return tok_low

def rem_stop_words(a):
    stop_words = set(stopwords.words('english'))
    set1=set(a)
    set2=set(stop_words)
    set3=set({'',""," "})
    return set1-set2-set3

def lemm(a,tag):
    lemmatizer = WordNetLemmatizer()
    b=[lemmatizer.lemmatize(w) for w in a]
    return b

def snow_stemm(a,tag):
    snow_stemmer = SnowballStemmer(language='english')
    b=[snow_stemmer.stem(w) for w in a]
    return b

def porter_stemm(a,tag):
    snow_stemmer = PorterStemmer()
    b=[snow_stemmer.stem(w) for w in a]
    return b

def pystemm(a,tag):
    pass