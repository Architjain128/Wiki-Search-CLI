import sys
import os
import xml.sax
from parse_sax import *
from config import *


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
    os.system("clear")
    def_msg("\n"+"="*50)
    dec_msg("Indexer started")
    n=len(sys.argv)
    if n != 4:
        error_msg("Arguments must be [ <dump_file_path> <invert_file_path> <invert_stat_file> ]")
        byexit(0)
    else:
        code_file,dump_path,invert_path,stat_file = sys.argv
        inp_msg("> Dump path set to "+dump_path)
        inp_msg("> Invert path set to "+invert_path)
        inp_msg("> Stat file set to "+stat_file)
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        Handler = Parser_sax()
        parser.setContentHandler(Handler)
        parser.parse(dump_path)
        byexit(1)



if __name__ == "__main__":
    init()