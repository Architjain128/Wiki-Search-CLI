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

def all_magic_happens_here(a,t=True,st=True):
    if t==True:
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

def present_format(a,t=True,st=True):
    arr=[]
    if t==True:
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
        # c=stemmer.stemWord(g)
        if (g not in stop_words)and(g!='' and len(g)>3):
            arr.append([g,"",1,[]])
        else :
            arr.append([g,"",-1,[]])
    # print(arr)
    return arr

def blank_search(path,query):
    return_list=[]
    kk=present_format(query,t=False)
    for g in kk:
        g[1]=stemmer.stemWord(g[0])
    gg=all_magic_happens_here(query)
    return [[],[],[],[],[],gg],kk

def field_search(path,query):
    title=[]
    info=[]
    catty=[]
    refer=[]
    extlink=[]
    other=[]
    kk=present_format(query,t=False)
    gg=all_magic_happens_here(query,False)
    fl="o"
    for g in kk:
        if g[2]==1:
            if( g[0][1]==':' and g[0][0]=='t'):
                g[0]=g[0][2:]
            elif( g[0][1]==':' and g[0][0]=='i'):
                g[0]=g[0][2:]
            elif( g[0][1]==':' and g[0][0]=='c'):
                g[0]=g[0][2:]
            elif( g[0][1]==':' and g[0][0]=='r'):
                g[0]=g[0][2:]
            elif( g[0][1]==':' and g[0][0]=='l'):
                g[0]=g[0][2:]
            elif( g[0][1]==':' and g[0][0]=='b'):
                g[0]=g[0][2:]
    for g in kk:
        g[1]=stemmer.stemWord(g[0])
        
    for g in gg:
        if len(g)>2:
            if( g[1]==':' and g[0]=='t'):
                title.append(g[2:])
                fl="t"
            elif( g[1]==':' and g[0]=='i'):
                info.append(g[2:])
                fl="i"
            elif( g[1]==':' and g[0]=='c'):
                catty.append(g[2:])
                fl="c"
            elif( g[1]==':' and g[0]=='r'):
                refer.append(g[2:])
                fl="r"
            elif( g[1]==':' and g[0]=='l'):
                extlink.append(g[2:])
                fl="l"
            elif( g[1]==':' and g[0]=='b'):
                other.append(g[2:])
                fl="o"
            else:
                if fl=="t":
                    title.append(g)
                elif fl=="i":
                    info.append(g)
                elif fl=="c":
                    catty.append(g)
                elif fl=="r":
                    refer.append(g)
                elif fl=="l":
                    extlink.append(g)
                else:
                    other.append(g)
    gg=[title,info,catty,refer,extlink,other]
    return gg,kk

def find_query(path,query):
    return_list=[]
    return_list2=[]
    a=query.split(":")
    if(len(a)>1):
        return_list,return_list2=field_search(path,query)
    else:
        return_list,return_list2=blank_search(path,query)
    return return_list,return_list2