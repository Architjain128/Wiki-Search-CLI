import xml.sax
from magic import *
from parse_cat import *

till_page = 0;

def imp_ck():
    print("hi");

class Parser_sax(xml.sax.ContentHandler):
    def __init__ (self):
        self.currentdata = ""
        self.data=""
        self.title=""
        self.text=""
    
    def startElement(self, tag, attrs):
        self.currentdata = tag
    
    def endElement(self, tag):
        global till_page
        if tag == "page":
            print(">"*21)
            parse_text_tag(self.text)
            print(">"*21)
            till_page+=1
            if till_page%100==0:
                aa=till_page*50//52622
                bb=50-aa;
                print( "done "+str(2*aa)+" % ["+"="*(aa)+">"+" "*bb+"]",end="\r")
        
        
        if self.currentdata == "title":
            self.title=""
        
        if self.currentdata == "text":
            pass
            # print("-"*100)
            # print(self.text)
            # print("-"*100)
            # self.text=""
        
        self.currentdata = ""
    
    def characters(self, content):
        if self.currentdata == "title":
            self.title += content
        if self.currentdata == "text":
            self.text += content
