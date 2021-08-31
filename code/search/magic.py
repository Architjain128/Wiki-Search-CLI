import nltk.corpus
import re
import nltk
import time
from nltk.corpus import stopwords
import Stemmer


stemmer = Stemmer.Stemmer('english')
stop_words = stopwords.words('english')

def re_tok(a):
    tok_low = re.split(r'[^A-Za-z0-9]+', a)
    return tok_low
def re_tok2(a):
    tok_low = re.split(r'[^A-Za-z0-9:]+', a)
    return tok_low

def all_magic_happens_here(a,st=True):
    if st==True:
        gg=re_tok(a)
    else: 
        gg=re_tok2(a)
    
    return_val=[]
    return_val1=[]
    if st==False:
        for c in gg:
            if c!='':
                return_val1.append(c)
        return return_val
    for g in gg:
        c=stemmer.stemWord(g)
        if (c not in stop_words)and(c!='' and len(c)>3):
            return_val.append(c)
    return return_val

def blank_search(path,query):
    return_list=[]
    gg=all_magic_happens_here(query)
    return gg

def field_search(path,query):
    return_list=[]
    title=[]
    info=[]
    catty=[]
    refer=[]
    extlink=[]
    other=[]
    
    gg=all_magic_happens_here(query,False)
    for g in gg:
        if len(g)>2 and g[1]==':':
            if(g[0]=='t'):
                title.append(g[2:])
            elif(g[0]=='i'):
                info.append(g[2:])
            elif(g[0]=='c'):
                catty.append(g[2:])
            elif(g[0]=='r'):
                refer.append(g[2:])
            elif(g[0]=='e'):
                extlink.append(g[2:])
            else:
                other.append(g)
    gg=[title,info,catty,refer,extlink,other]
    return gg

def find_query(path,query):
    return_list=[]
    a=query.split(":")
    if(len(a)>1):
        return_list+=blank_search(path,query)
    else:
        return_list+=field_search(path,query)
    return return_list