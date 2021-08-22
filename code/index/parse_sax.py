import xml.sax

def imp_ck():
    print("hi");

class Parser_sax(xml.sax.ContentHandler):
    def __init__ (self):
        self.currentdata = ""
        self.page = ""
        self.title = ""
    
    def startElement(self, tag, attrs):
        self.currentdata = tag
        if tag == "page":
            print("-"*20+"PAGE START"+"-"*20)
            # print(attrs)
    
    def endElement(self, tag):
        if self.currentdata == "title":
            print("Title : "+self.title)
        self.currentdata = ""
    
    def characters(self, content):
        if self.currentdata == "title":
            self.title = content