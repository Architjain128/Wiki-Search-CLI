import re
from config import *

# parse xml <text>...</text> in a wikipedia page into infobox,categories, external links and references
def parse_text_tag(a):
    
    infoboxes = re.findall(r"\{\{Infobox (.*?)\}\}[\r\n]", str(a), flags=re.DOTALL)
    body = re.sub(r"\{\{Infobox (.*?)\}\}[\r\n]", "", str(a), flags=re.DOTALL)
    
    categories = re.findall(r"\[\[Category:(.*)\]\]", str(body), flags=re.DOTALL)
    body = re.sub(r"\[\[Category:(.*)\]\]", "", str(body), flags=re.DOTALL)
    
    
    bibliography = re.findall(r"\*\{\{cite(.*?)\}\}", str(body), flags=re.DOTALL)
    body = re.sub(r"\*\{\{cite(.*?)\}\}","", str(body), flags=re.DOTALL)
    
    external_links = re.findall(r"==External links==(.*)", str(body), flags=re.DOTALL)
    body = re.sub(r"==External links==(.*)","", str(body), flags=re.DOTALL)
    
    references = re.findall(r"==References==(.*)\}\}", str(body), flags=re.DOTALL)
    body = re.sub(r"==References==(.*)\}\}","", str(body), flags=re.DOTALL)
    
   

    val=[infoboxes, categories, external_links, bibliography,references,body]
    for a in val:
        # print(a)
        print(re.split(r'[^A-Za-z0-9]+', str(a).strip()))
        print()
    return val