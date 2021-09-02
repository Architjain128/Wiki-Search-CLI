import os
import sys
import json
from magic import *
from config import *

# if geek_mode==False:
    # from tabulate import tabulate

dic_title={}
inv_dic={}

def hex_int(a):
    a="0x"+a
    return int(a,16)

# def dec_msg(a):
#     if colo==True:
#         print(Fore.MAGENTA+a+RESET)
#     elif msg==True:
#         print(a)

# def error_msg(a):
#     if colo==True:
#         print(Fore.RED+a+RESET)
#     elif msg==True:
#         print(a)

# def warning_msg(a):
#     if colo==True:
#         print(Fore.YELLOW+a+RESET)
#     elif msg==True:
#         print(a)

# def sucess_msg(a):
#     if colo==True:
#         print(Fore.GREEN+a+RESET)
#     elif msg==True:
#         print(a)

# def res_msg(a):
#     if colo==True:
#         print(Fore.LIGHTGREEN_EX+a+RESET)
#     elif msg==True:
#         print(a)

# def inp_msg(a):
#     if colo==True:
#         print(Fore.BLUE+a+RESET)
#     elif msg==True:
#         print(a)

# def def_msg(a):
#     if colo==True:
#         print(Fore.WHITE+a+RESET)
#     elif msg==True:
#         print(a)

def intersection(a,b):
    if(len(b))==0:
        return a
    temp = set(b)
    c = [value for value in a if value in temp]
    return c

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

# def byexit(a):
#     if a==1:
#         sucess_msg("exited successfully")
#     if a==0:
#         error_msg("exited abruptly")
#     def_msg("="*80+"\n")

def create_list(gg):
    title=[]
    info=[]
    catty=[]
    refer=[]
    extlink=[]
    other=[]
    for i in range(len(gg)):
        val=[]
        for j in gg[i]:
            if (j in inv_dic) and inv_dic[j][i]!=['']:
                val=union(val,inv_dic[j][i])
            # else:
                # warning_msg("Warning : ["+j+"] not found in the index")
        if i==0:
            title=val
        elif i==1:
            info=val
        elif i==2:
            catty=val
        elif i==3:
            refer=val
        elif i==4:
            extlink=val
        elif i==5:
            other=val
    return [title,info,catty,refer,extlink,other]

def read_files(path):
    # fp1=open(str(path+"/titles/0.txt"),'r')
    fp2=open(str(path+"/inv/0.txt"),'r')
    global dic_title
    global inv_dic
    lines1 = fp1.readlines()
    for line in lines1:
        a=line.strip('\n')
        a=a.split("<@>")
        dic_title[a[0]]=a[1]
    lines2 = fp2.readlines()
    for line in lines2:
        a=line.strip('\n')
        a=a.split(" ",1)
        b=a[1].split(";")
        c=[]
        for xx in b:
            cc=xx.split(",")
            c.append(cc)
        inv_dic[a[0]]=[c[0],c[1],c[2],c[3],c[4],c[5]]
    fp1.close()
    fp2.close()

def id_to_title(id):
    if id in dic_title:
        return dic_title[id]
    else:
        return "Not found"

n=len(sys.argv)
# os.system("clear")
# print("="*80)
if n != 3:
    pass
    # error_msg("Improper argument passed"+str(sys.argv)+str(n))
    # byexit(0)
else:
    code_file,invert_path,query_string = sys.argv
    # inp_msg("> Invert path set to "+invert_path)
    # inp_msg("> Searching for [ "+query_string+" ]")
    # dec_msg("Reading Inverted file : Please wait, this may take a while ...")
    read_files(invert_path)
    # dec_msg("Finding results for your query ...")
    search_list=[]
    search_list2=[]
    temp,temp2=find_query(invert_path,query_string.lower())
    search_list+=temp
    search_list2+=temp2
    
    if geek_mode==False:
        lis=create_list(search_list)
        final_ids=[]
        for x in lis:
            final_ids=union(final_ids,x)
        if len(final_ids)==0:
            pass
            # error_msg("No results found")
            # byexit(1)
        else :
            if len(final_ids)>10:
                pass
                # warning_msg("More than 10 results found, showing only 10 results")
                final_ids=final_ids[:10]
            # sucess_msg("Search results are :")
            i=0
            data=[]
            for x in final_ids:
                i+=1
                data.append([i,x,id_to_title(x)])
                # res_msg(str(i)+" > "+str(x)+" | "+id_to_title(x))
            # print(tabulate(data,headers=['No.','ID','Title'],tablefmt="fancy_grid"))
            print(data)
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
        # print(search_list2)
        # print(arr)
        json_data=json.dumps(arr)
        json_object = json.loads(json_data)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
        # byexit(1)
