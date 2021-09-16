import xml.sax
from magic import *
from parse_tags import *
from invertindex import *

till_page = 0
stat1=0
stat2=0
hex_id=""
titit=[]
class Parser_sax(xml.sax.ContentHandler):
    def __init__ (self,path,file):
        self.currentdata = ""
        self.path=path
        self.data=""
        self.title=""
        self.text=""
        self.id="NaN"
        self.titi=[]
        self.tit_file=0
        self.file=file
        self.okok=0
        print(path)
        
        
        
    def startElement(self, tag, attrs):
        self.currentdata = tag
        if tag=="title":
            self.title =""
        if tag=="text":
            self.text =""
    
    def endElement(self, tag):
        global till_page
        global stat1
        global stat2
        global titit
        global hex_id
        if tag == "page":
            hex_id=hex(till_page)
            hex_id=hex_id[2:]
            needed_to_be_indexed=parse_baby_parse(self.id,self.title, self.text)
            stat1 += needed_to_be_indexed[-1]
            needed_to_be_indexed.pop()
            deal_with_dump(hex_id,needed_to_be_indexed)
            self.titi.append([hex_id,self.title.strip()])
            till_page+=1
            
            if till_page%Doc_id_Limit==0:
                write_title(self.path,self.titi,self.tit_file)
                stat2+=give_me_final_dump(self.path,self.okok)
                # self.fp.write(self.title+"\n")
                titit.append(hex_id)
                self.titi=[]
                self.okok+=1
                self.tit_file+=1
            if till_page%100==0:
                print(str(till_page)+" done",end="\r")

        if tag=="mediawiki":
            write_title(self.path,self.titi,self.tit_file)
            stat2=give_me_final_dump(self.path,self.okok)
            self.titi=[]
            # fs=open(self.file,"w")
            # print(stat1,stat2,file=fs,sep="\n")
            # fs.close()
            fp=open(self.path+"/titles/log.txt",'w')
            for x in titit:
                print(x,file=fp)
            fp.close()
            fp=open(self.path+"/titles/count.txt",'w')
            print(hex_id,file=fp)
            fp.close()
            print( str(till_page)+" done.",end="\n")

    def characters(self, content):
        if self.currentdata == "title":
            self.title += content
        if self.currentdata == "text":
            self.text += content
        
