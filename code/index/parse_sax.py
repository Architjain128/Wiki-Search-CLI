import xml.sax
from magic import *
from parse_tags import *
from invertindex import *

till_page = 0;
class Parser_sax(xml.sax.ContentHandler):
    def __init__ (self,path):
        self.currentdata = ""
        self.path=path
        self.data=""
        self.title=""
        self.text=""
        self.id="NaN"
        self.titi=[]
        self.tit_file=0
    
    def startElement(self, tag, attrs):
        self.currentdata = tag
        if tag=="title":
            self.title =""
        if tag=="text":
            self.text =""
    
    def endElement(self, tag):
        global till_page
        if tag == "page":
            
            hex_id=hex(till_page)
            hex_id=hex_id[2:]
            # hex_id=till_page
            needed_to_be_indexed=parse_baby_parse(self.id,self.title, self.text)
            deal_with_dump(hex_id,needed_to_be_indexed)
            # make inverted index
            if till_page!=0 and till_page%Doc_id_Limit==0:
                write_title(self.path,self.titi,self.tit_file)
                self.tit_file+=1
                self.titi=[]
                
            self.titi.append([hex_id,self.title.strip()])
            till_page+=1
            
            
            if till_page%500==0:
                aa=till_page*50//52622
                bb=50-aa;
                print( str(till_page)+" done or "+str(2*aa)+" % ["+"="*(aa)+">"+" "*bb+"]",end="\r")

        if tag=="mediawiki":
            write_title(self.path,self.titi,self.tit_file)
            give_me_final_dump(self.path)
            self.tit_file+=1
            self.titi=[]
            print( str(till_page)+" done or 100 % [" + str("="*50) +">]",end="\n")

    def characters(self, content):
        if self.currentdata == "title":
            self.title += content
        if self.currentdata == "text":
            self.text += content
        
