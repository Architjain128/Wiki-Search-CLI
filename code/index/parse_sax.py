import xml.sax
from magic import *


till_page = 0;

def imp_ck():
    print("hi");

class Parser_sax(xml.sax.ContentHandler):
    def __init__ (self):
        self.currentdata = ""
        self.page = ""
        self.title = ""
        self.text = ""
    
    def startElement(self, tag, attrs):
        self.currentdata = tag
    
    def endElement(self, tag):
        global till_page
        if tag == "page":
            till_page+=1
            if till_page%100==0:
                aa=till_page*50//52622
                bb=50-aa;
                print( "done "+str(aa)+" % ["+"="*(aa)+">"+" "*bb+"]",end="\r")
        if self.currentdata == "title":
            list_of_words=all_magic_happens_here(self.title,"title")
            self.title=""
        if self.currentdata == "text":
            list_of_words=all_magic_happens_here(self.text,"text")
            self.text=""
        self.currentdata = ""
    
    def characters(self, content):
        if self.currentdata == "title":
            self.title += content
        if self.currentdata == "text":
            self.text+=content
