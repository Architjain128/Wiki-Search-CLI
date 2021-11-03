import os
import sys
import json
from magic import *
from config import *
import bisect
import math
import time

if geek_mode==False:
    from tabulate import tabulate

dic_title={}
inv_dic={}
tree_tit=[]
tree_inv=[]
wt = {'0': 100,'1':60 ,'2': 25, '3': 15,'4': 15 ,'5': 10,'6':10}
scores={}
tot=0 

def getlog(path):
    global tot
    fp=open(path+"/titles/count.txt",'r')
    lines=fp.readlines()
    tot=hex_int(lines[0])

def hex_int(a):
    a="0x"+a
    return int(a,16)

def dec_msg(a):
    if colo==True:
        print(Fore.MAGENTA+a+RESET)
    elif msg==True:
        print(a)

def error_msg(a):
    if colo==True:
        print(Fore.RED+a+RESET)
    elif msg==True:
        print(a)

def warning_msg(a):
    if colo==True:
        print(Fore.YELLOW+a+RESET)
    elif msg==True:
        print(a)

def sucess_msg(a):
    if colo==True:
        print(Fore.GREEN+a+RESET)
    elif msg==True:
        print(a)

def res_msg(a):
    if colo==True:
        print(Fore.LIGHTGREEN_EX+a+RESET)
    elif msg==True:
        print(a)

def inp_msg(a):
    if colo==True:
        print(Fore.BLUE+a+RESET)
    elif msg==True:
        print(a)

def def_msg(a):
    if colo==True:
        print(Fore.WHITE+a+RESET)
    elif msg==True:
        print(a)

def intersection(a,b):
    if(len(b))==0:
        return a
    temp = set(b)
    c = [value for value in a if value in temp]
    return c

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def byexit(a):
    if a==1:
        sucess_msg("exited successfully")
    if a==0:
        error_msg("exited abruptly")
    def_msg("="*80+"\n")

def tfidf_score(data,filed):
    global wt
    data=data.split(";")
    fre_num=0
    doc_fre_num=0
    b=[]
    c=[]
    dic={}
    for xx in data:
        ccc=xx.split(",")
        for x in ccc:
            cc=x.split("-")
            if len(cc)==2:
                c.append(cc[0])
                doc_fre_num+=1
                b.append(cc[1])
                fre_num+=int(cc[1])
                if cc[0] in dic:
                    dic[cc[0]]=int(dic[cc[0]])+int(cc[1])
                else:
                    dic[cc[0]]=cc[1]
    idf=math.log(int(tot)/int(doc_fre_num))
    for did in dic:
        tf=math.log(1+int(dic[did]))
        dic[did]=tf*idf*wt[str(filed)]
    return dic

def create_list(path,j,i):
    temp_dic={}
    aaa=bisect.bisect_left(tree_inv,j,0,len(tree_inv))
    fp=open(path+"/merged/A"+str(aaa)+".txt",'r')
    found=False
    lines=fp.readlines()
    for line in lines:
        a=line.strip('\n')
        a=a.split(" ",1)
        if a[0]==j:
            found=True
            return tfidf_score(a[1],i)
    if found==False:
        warning_msg("Warning : ["+j+"] not found in the index")
        return {}
    return {}

def search_proffesor(path,gg):
    global scores
    for i in range(len(gg)):
        for j in gg[i]:
            ttt=create_list(path,j,i)
            for did in ttt:
                if did in scores:
                    scores[did]+=ttt[did]
                else:
                    scores[did]=ttt[did]

def read_files(path):
    fp2=open(str(path+"/merged/log.txt"),'r')
    global tree_inv
    lines2 = fp2.readlines()
    for line in lines2:
        a=line.strip('\n')
        a=a.split(" ",1)
        tree_inv.append(a[0])
    fp2.close()
    fp3=open(str(path+"/titles/log.txt"),'r')
    global tree_tit
    lines2 = fp3.readlines()
    for line in lines2:
        a=line.strip('\n')
        tree_tit.append(hex_int(a))
    fp3.close()
    # print(tree_tit)
    
def id_to_title(path,id):
    iid=id
    id=hex_int(id)
    if id>tot:
        return "Not found"
    else:
        aaa=bisect.bisect_left(tree_tit,id,0,len(tree_tit))
        fp=open(path+"/titles/"+str(aaa)+".txt",'r')
        found=False
        lines=fp.readlines()
        for line in lines:
            a=line.strip('\n')
            a=a.split("<@>",1)
            if a[0]==iid:
                found=True
                return a[1]
        if found==False:
            warning_msg("Warning : ["+str(id)+"] not found in the index")
            return "Not found"

n=len(sys.argv)
os.system("clear")
print("="*80)

if TEST==True:
    if n != 4:
        error_msg("Improper argument passed"+str(sys.argv)+str(n))
        byexit(0)
    else :
        code_file,invert_path,query_path,query_out = sys.argv
        
        inp_msg("> Invert path location set to "+invert_path)
        dec_msg("Reading Inverted file : Please wait, this may take a while ...")
        read_files(invert_path)
        getlog(invert_path)
        qp=open(query_path,'r')
        qop=open(query_out,'w')
        liness=qp.readlines()
        for query_string in liness:
            query_string=query_string.strip()
            inp_msg("> Searching for [ "+query_string+" ]")
            scores={}
            search_list=[]
            search_list2=[]
            start_time=time.time()
            temp,temp2=find_query(invert_path,query_string.lower())
            search_list+=temp
            search_list2+=temp2
            
            if geek_mode==False:
                search_proffesor(invert_path,search_list)
                final_ids=[]
                for i in sorted(scores, key=scores.get, reverse=True):
                    final_ids.append(i)
                if len(final_ids)==0:
                    error_msg("No results found")
                    # byexit(1)
                else :
                    if len(final_ids)>10:
                        # warning_msg("More than 10 results found, showing only 10 results")
                        final_ids=final_ids[:10]
                    # sucess_msg("Search results are :")
                    i=0
                    data=[]
                    for x in final_ids:
                        i+=1
                        nam=id_to_title(invert_path,x)
                        data.append([i,x,nam])
                        qop.write(x+", "+nam+"\n")
                        
                qop.write(str(time.time()-start_time)+"\n\n")
                        # res_msg(str(i)+" > "+str(x)+" | "+nam)
                    # print(tabulate(data,headers=['No.','ID','Title'],tablefmt="fancy_grid"))
                    # print(data)
                    # byexit(1)
            else :
                arr=[]
                no_res={
                    "title":["NO RESULTS FOUND"],
                    "infobox":["NO RESULTS FOUND"],
                    "categories":["NO RESULTS FOUND"],
                    "references":["NO RESULTS FOUND"],
                    "external link":["NO RESULTS FOUND"],
                    "body":["NO RESULTS FOUND"]
                }
                temp={
                    "title":[],
                    "infobox":[],
                    "categories":[],
                    "references":[],
                    "external link":[],
                    "body":[]
                }
                for k in search_list2:
                    if k[2]==-1:
                        arr.append({k[0]:no_res})
                    elif (k[1] not in inv_dic):
                        arr.append({k[0]:no_res})
                    else:
                        tmp=temp
                        if inv_dic[k[1]][0]!=[] and inv_dic[k[1]][0]!=['']:
                            tmp["title"]=inv_dic[k[1]][0]
                        if inv_dic[k[1]][1]!=[] and inv_dic[k[1]][1]!=['']:
                            tmp["infobox"]=inv_dic[k[1]][1]
                        if inv_dic[k[1]][2]!=[] and inv_dic[k[1]][2]!=['']:
                            tmp["categories"]=inv_dic[k[1]][2]
                        if inv_dic[k[1]][3]!=[] and inv_dic[k[1]][3]!=['']:
                            tmp["references"]=inv_dic[k[1]][3]
                        if inv_dic[k[1]][4]!=[] and inv_dic[k[1]][4]!=['']:
                            tmp["external link"]=inv_dic[k[1]][4]
                        if inv_dic[k[1]][5]!=[] and inv_dic[k[1]][5]!=['']:
                            tmp["body"]=inv_dic[k[1]][5]
                        arr.append({k[0]:tmp})
                print(search_list2)
                print(arr)
                json_data=json.dumps(arr)
                json_object = json.loads(json_data)
                json_formatted_str = json.dumps(json_object, indent=2)
                print(json_formatted_str)
                # byexit(1)
        qop.close()
else:
    if n != 2:
        error_msg("Improper argument passed"+str(sys.argv)+str(n))
        byexit(0)
    else :
        code_file, query_path = sys.argv
        invert_path="./small"
        inp_msg("> Invert path location set to "+invert_path)
        dec_msg("Reading Inverted file : Please wait, this may take a while ...")
        read_files(invert_path)
        getlog(invert_path)
        qp=open(query_path,'r')
        qqq=query_path[:-4]+"_op10.txt"
        print(qqq)
        qop=open(qqq,'w')
        liness=qp.readlines()
        for query_string in liness:
            query_string=query_string.strip()
            inp_msg("> Searching for [ "+query_string+" ]")
            scores={}
            search_list=[]
            search_list2=[]
            start_time=time.time()
            temp,temp2=find_query(invert_path,query_string.lower())
            search_list+=temp
            search_list2+=temp2
            
            if geek_mode==False:
                search_proffesor(invert_path,search_list)
                final_ids=[]
                for i in sorted(scores, key=scores.get, reverse=True):
                    final_ids.append(i)
                if len(final_ids)==0:
                    error_msg("No results found")
                    # byexit(1)
                else :
                    if len(final_ids)>10:
                        warning_msg("More than 10 results found, showing only 10 results")
                        final_ids=final_ids[:10]
                    sucess_msg("Search results are :")
                    i=0
                    data=[]
                    for x in final_ids:
                        i+=1
                        nam=id_to_title(invert_path,x)
                        data.append([i,x,nam])
                        qop.write(x+", "+nam+"\n")
                        
                qop.write(str(time.time()-start_time)+"\n\n")
                        # res_msg(str(i)+" > "+str(x)+" | "+nam)
                    # print(tabulate(data,headers=['No.','ID','Title'],tablefmt="fancy_grid"))
                    # print(data)
                    # byexit(1)
            else :
                arr=[]
                no_res={
                    "title":["NO RESULTS FOUND"],
                    "infobox":["NO RESULTS FOUND"],
                    "categories":["NO RESULTS FOUND"],
                    "references":["NO RESULTS FOUND"],
                    "external link":["NO RESULTS FOUND"],
                    "body":["NO RESULTS FOUND"]
                }
                temp={
                    "title":[],
                    "infobox":[],
                    "categories":[],
                    "references":[],
                    "external link":[],
                    "body":[]
                }
                for k in search_list2:
                    if k[2]==-1:
                        arr.append({k[0]:no_res})
                    elif (k[1] not in inv_dic):
                        arr.append({k[0]:no_res})
                    else:
                        tmp=temp
                        if inv_dic[k[1]][0]!=[] and inv_dic[k[1]][0]!=['']:
                            tmp["title"]=inv_dic[k[1]][0]
                        if inv_dic[k[1]][1]!=[] and inv_dic[k[1]][1]!=['']:
                            tmp["infobox"]=inv_dic[k[1]][1]
                        if inv_dic[k[1]][2]!=[] and inv_dic[k[1]][2]!=['']:
                            tmp["categories"]=inv_dic[k[1]][2]
                        if inv_dic[k[1]][3]!=[] and inv_dic[k[1]][3]!=['']:
                            tmp["references"]=inv_dic[k[1]][3]
                        if inv_dic[k[1]][4]!=[] and inv_dic[k[1]][4]!=['']:
                            tmp["external link"]=inv_dic[k[1]][4]
                        if inv_dic[k[1]][5]!=[] and inv_dic[k[1]][5]!=['']:
                            tmp["body"]=inv_dic[k[1]][5]
                        arr.append({k[0]:tmp})
                print(search_list2)
                print(arr)
                json_data=json.dumps(arr)
                json_object = json.loads(json_data)
                json_formatted_str = json.dumps(json_object, indent=2)
                print(json_formatted_str)
                # byexit(1)
        qop.close()
    