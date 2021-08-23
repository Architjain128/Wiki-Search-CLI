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

STOP_WORDS=["reflist","refbegin","refend","-->","|","[[Category:","{{Infobox"]

def all_magic_happens_here(a,tag,fl=0):
    list_of_all_lowecase_words = re_tok_lower(a,tag)
    if fl==0:
        words=lemm(list_of_all_lowecase_words,tag)
    if fl ==1:
        words=porter_stemm(list_of_all_lowecase_words,tag)
    if fl ==2:
        words=snow_stemm(list_of_all_lowecase_words,tag)
    set_non_stop_words=rem_stop_words(words)
    return list_of_all_lowecase_words


def re_tok_lower(a,tag):
    tok_low = re.split(r'[^A-Za-z0-9]+', a.strip().lower())
    return tok_low

def rem_stop_words(a):
    stop_words = set(stopwords.words('english'))
    print(stop_words)
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