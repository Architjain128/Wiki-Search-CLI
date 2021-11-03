import os
import sys
import time
import xml.sax
import shutil
from config import *
from parse_sax import *
from invertindex import *
from merge import *
from staty import *

global global_index_path
stat1=0

def dec_msg(a):
    if colo==True:
        print(Fore.MAGENTA+a+RESET)
    else:
        print(a)

def error_msg(a):
    if colo==True:
        print(Fore.RED+a+RESET)
    else:
        print(a)

def warning_msg(a):
    if colo==True:
        print(Fore.YELLOW+a+RESET)
    else:
        print(a)

def sucess_msg(a):
    if colo==True:
        print(Fore.GREEN+a+RESET)
    else:
        print(a)

def inp_msg(a):
    if colo==True:
        print(Fore.BLUE+a+RESET)
    else:
        print(a)

def def_msg(a):
    if colo==True:
        print(Fore.WHITE+a+RESET)
    else:
        print(a)


def byexit(a):
    if a==1:
        sucess_msg("Indexer exited successfully")
    if a==0:
        error_msg("Indexer exited abruptly")
    def_msg("="*50+"\n")


def init():
    global stat1
    os.system("clear")
    def_msg("\n"+"="*50)
    dec_msg("Indexer started")
    n=len(sys.argv)
    if n != 4:
        pass
        error_msg("Arguments must be [ <dump_file_path> <invert_file_path> <invert_stat_file> ]")
        byexit(0)
    else:
        code_file,dump_path,invert_path,stat_file = sys.argv
        inp_msg("> Dump path set to "+dump_path)
        inp_msg("> Invert path set to "+invert_path)
        inp_msg("> Stat file set to "+stat_file)
        try:
            os.stat(invert_path)
        except:
            os.mkdir(invert_path)
        try:
            os.stat(invert_path+"/titles")
        except:
            os.mkdir(invert_path+"/titles")
        try:
            os.stat(invert_path+"/inv")
        except:
            os.mkdir(invert_path+"/inv")
        try:
            os.stat(invert_path+"/merged")
        except:
            os.mkdir(invert_path+"/merged")
            
        aa=time.time()
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        Handler = Parser_sax(invert_path,stat_file)
        parser.setContentHandler(Handler)
        parser.parse(open(dump_path,'r'))
        
        path=invert_path+"/inv/"
        path2=invert_path+"/merged/"
        lsit=[]
        ap=os.listdir(path)
        for a in ap:
            lsit.append(path+a)
        a=mergeSortedFiles(path,lsit,path2)
        
        print(time.time()-aa)
        mydir = invert_path+"/inv"
        shutil.rmtree(mydir)
        stat1= get_size_format(get_directory_size(invert_path))
        stat2=get_num_files(invert_path)
        stat3=a
        fs=open(stat_file,"w")
        print(stat1,stat2,stat3,file=fs,sep="\n")
        fs.close()
        byexit(1)

if __name__ == "__main__":
    init()
    
