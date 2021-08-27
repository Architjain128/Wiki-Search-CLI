import re
from config import *
from magic import *

tag_d=[""]*10
tag_d[0]="id"
tag_d[1]="title"
tag_d[2]="infobox"
tag_d[3]="categories"
tag_d[4]="external"
tag_d[5]="reference"
tag_d[6]="extra_body"

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
    
    # parse_references(text)
    get_ref(text)
    
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

def get_ref(data):
    refs = []
    for m in re.finditer(r'==\s*references\s*==', data):
        n = re.search(r'==[a-z ]*==', data[m.start()+5:])
        if n:
            refs = refs + all_magic_happens_here(data[m.start():n.end()],"refer")
        else:
            refs = refs + all_magic_happens_here(data[m.start():],"refer")
            break
    return refs

def parse_references(a):
    return_val=[]
    a=a.split("==references==")
    if len(a)>1:
        if len(a)>2:
            print("WTF1")
        else:
            a=a[1].split("{{refbegin")
            if len(a)>1:
                if  len(a)>2:
                    print("WTF2")
                else :
                    a=a[1].split("refend")
                    for i in range(1,len(a)):
                        temp=a[i].split("\n")
                        for tt in temp:
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

def parse_text_tag(a):
    
    bibliography = re.findall(r"\*\{\{cite(.*?)\}\}", str(body), flags=re.DOTALL)
    body = re.sub(r"\*\{\{cite(.*?)\}\}","", str(body), flags=re.DOTALL)
    
    references = re.findall(r"=references==(.*)\}\}", str(body), flags=re.DOTALL)
    body = re.sub(r"==references==(.*)\}\}","", str(body), flags=re.DOTALL)