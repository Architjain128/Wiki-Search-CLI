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
        self.id=""
        self.idfl=False
    
    def startElement(self, tag, attrs):
        self.currentdata = tag
        if tag=="id" and self.idfl==False:
            self.id =""
        if tag=="title":
            self.title =""
        if tag=="text":
            self.text =""
    
    def endElement(self, tag):
        global till_page
        if tag == "page":
            j=parse_baby_parse(self.id,self.title, self.text)
            
            till_page+=1
            if(till_page==28310):
                print(self.id)
                
            if till_page%500==0:
                print(str(till_page)+"\r")
            
            self.idfl=False
            #     aa=till_page*50//52622
            #     bb=50-aa;
            #     print( "done "+str(2*aa)+" % ["+"="*(aa)+">"+" "*bb+"]",end="\r")
            
    def characters(self, content):
        if self.currentdata == "title":
            self.title += content
        if self.currentdata == "text":
            self.text += content
        if self.currentdata == "id" and self.idfl==False:
            self.id = content
            self.idfl=True
