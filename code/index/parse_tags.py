import re
from config import *
from magic import *
import time

def parse_baby_parse(pid,title,text):
    return_val=[]
    return_val.append(pid)
    title=title.lower()
    text=text.lower()
    ctr=0
    
    title,vv = parse_title_tag(title)
    return_val.append(title)
    ctr+=vv
    
    info,vv = parse_infobox(text)
    return_val.append(info)
    ctr+=vv
    
    catty,vv=parse_catty(text)
    return_val.append(catty)
    ctr+=vv
    
    extlink,vv=parse_extlink(text)
    return_val.append(extlink)
    ctr+=vv
    
    # refer=parse_references(text)
    refer,vv=get_ref(text)
    return_val.append(refer)
    ctr+=vv
    
    body,vv=parse_bypass(text)
    return_val.append(body)
    ctr+=vv
    
    return_val.append(ctr)
    
    return return_val

def parse_title_tag(a):
    return all_magic_happens_here(a,"title")

def parse_bypass(a):
    return_val=[]
    temp=a.split("\n")
    fl=False
    x=0
    for tt in temp:
        if tt=="|}":
            fl=True
        elif fl==True and tt.find( "==references==" )!=-1:
            break
        elif fl==True and tt.find( "==external links==" )!=-1:
            break
        elif fl==True and tt.find( "[[category:" )!=-1 :
            break
        elif fl==True:
            cc,cd=re_tok(tt)
            return_val+=cc
            x+=cd
    return stemm(return_val),x

def get_ref(data):
    refs = []
    x=0
    for m in re.finditer(r'==\s*references\s*==', data):
        n = re.search(r'==[a-z ]*==', data[m.start()+5:])
        if n:
            cc,cd=re_tok(data[m.start():n.end()])
            refs = refs + cc
            x+=cd
        else:
            cc,cd=re_tok(data[m.start():])
            refs = refs + cc
            x+=cd
            break
    return stemm(refs),x

def parse_infobox(a):
    return_val=[]
    x=0
    a=a.split("{{infobox")
    for i in range(1,len(a)):
        temp=a[i].split("\n")
        for tt in temp:
            if tt=="}}":
                break
            else:
                cc,cd=all_magic_happens_here(tt,"infobox")
                return_val+=cc
                x+=cd
    return return_val,x

def parse_catty(a):
    category_list = re.findall(r"\[\[category:(.*)\]\]",a)
    return all_magic_happens_here(' '.join(category_list),"catty")

def parse_references(a):
    return_val=[]
    b=a
    x=0
    a=a.split("==references==")
    if len(a)>1:
        for i in range(1,len(a)):
            temp=a[i].split("{{refbegin")
            if len(temp)>1:
                for j in range(1,len(temp)):
                    ttt=temp[1].split("refend")
                    for i in range(1,len(ttt)):
                        tk=ttt[i].split("\n")
                        for tt in tk:
                            if tt and tt[0]!="*":
                                break
                            else:
                                cc,cd=all_magic_happens_here(tt,"refer")
                                return_val+=cc
                                x+=cd
    return return_val,x

def parse_extlink(a):
    return_val=[]
    x=0
    a=a.split("==external links==")
    for i in range(1,len(a)):
        temp=a[i].split("\n")
        for tt in temp:
            if tt and tt[0]=="*":
                cc,cd=all_magic_happens_here(tt,"extlink")
                return_val+=cc
                x+=cd
    return return_val,x

def parse_all_text(a):
    return all_magic_happens_here(a,"text")