import re
from config import *
from magic import *

def parse_baby_parse(pid,title,text):
    return_val=[]
    return_val.append(pid)
    title=title.lower()
    text=text.lower()

    title = parse_title_tag(title)
    return_val.append(title)
    
    info = parse_infobox(text)
    return_val.append(info)
    
    catty=parse_catty(text)
    return_val.append(catty)
    
    extlink=parse_extlink(text)
    return_val.append(extlink)
    
    refer=parse_references(text)
    return_val.append(refer)
    
    body,ctr=parse_all_text(text)
    return_val.append(body)
    return_val.append(ctr)
    
    return return_val

def parse_title_tag(a):
    a=all_magic_happens_here(a,"title",False)
    return a

def parse_infobox(a):
    return_val=[]
    a=a.split("{{infobox")
    count=len(a)
    for i in range(1,count):
        temp=a[i].split("\n")
        for tt in temp:
            if tt=="}}":
                break
            else:
                return_val+=all_magic_happens_here(tt,"infobox")
    return return_val

def parse_catty(a):
    category_list = re.findall(r"\[\[category:(.*)\]\]",a)
    return (all_magic_happens_here(' '.join(category_list),"catty"))

def parse_references(a):
    return_val=[]
    b=a
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
                                return_val+=all_magic_happens_here(tt,"refer")
    return return_val

def parse_extlink(a):
    return_val=[]
    a=a.split("==external links==")
    for i in range(1,len(a)):
        temp=a[i].split("\n")
        for tt in temp:
            if tt and tt[0]!="*":
                break
            else:
                return_val+=all_magic_happens_here(tt,"extlink")
    return return_val

def parse_all_text(a):
    gg= all_magic_happens_here(a,"text")
    return gg,len(gg)