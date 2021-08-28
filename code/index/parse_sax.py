import xml.sax
from magic import *
from parse_tags import *

till_page = 0;

class Parser_sax(xml.sax.ContentHandler):
    def __init__ (self):
        self.currentdata = ""
        self.data=""
        self.title=""
        self.text=""
        self.id="NaN"
    
    def startElement(self, tag, attrs):
        self.currentdata = tag
        if tag=="title":
            self.title =""
        if tag=="text":
            self.text =""
    
    def endElement(self, tag):
        global till_page
        if tag == "page":
            needed_to_be_indexed=parse_baby_parse(self.id,self.title, self.text)
            # make inverted index
            till_page+=1
            if till_page%500==0:
                aa=till_page*50//52622
                bb=50-aa;
                print( str(till_page)+" done or "+str(2*aa)+" % ["+"="*(aa)+">"+" "*bb+"]",end="\r")

        if tag=="mediawiki":
            print( str(till_page)+" done or 100 % [" + str("="*50) +">]",end="\n")

    def characters(self, content):
        if self.currentdata == "title":
            self.title += content
        if self.currentdata == "text":
            self.text += content
        
