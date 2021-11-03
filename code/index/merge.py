import sys
import heapq
import os
from config import *

def decorated_file(f, key):
    for line in f:
        yield (key(line), line)

def splity(line):
    a=line.strip('\n')
    a=a.split(" ",1)
    b=a[1].split(";")
    c=[]
    for xx in b:
        cc=xx.split(",")
        c.append(cc)
    return [a[0],c[0],c[1],c[2],c[3],c[4],c[5]]

def standard_keyfunc(line):
    a=line.strip('\n')
    a=a.split(" ",1)
    b=a[1].split(";")
    c=[]
    for xx in b:
        cc=xx.split(",")
        c.append(cc)
    return a[0],[c[0],c[1],c[2],c[3],c[4],c[5]]


def join_baba(t,u):
    v=[]
    for i in range(len(t)):
        temp=[]
        if t[i]!=['']:
            temp+=t[i]
        if u[i]!=['']:
            temp+=u[i]
        v.append(temp)
    return v

def sigma_rule(arr):
    aa=""
    for i in arr:
        aa+=((",").join(i))+";"
    return aa

def mergeSortedFiles(path,paths, output_path, dedup=True, keyfunc=standard_keyfunc):
    log_file=open(str(output_path)+"log.txt","w")
    file_num=0
    files = map(open, paths)   #open defaults to mode='r'
    output_file = open(output_path+"A"+str(file_num)+".txt", 'w')
    lines_written = 0
    pre_cmp = "<@@>"
    pre_line=[[''],[''],[''],[''],[''],['']]
    strrp=""
    pp=0
    for line in heapq.merge(*[decorated_file(f, keyfunc) for f in files]):
        cmp = line[0][0]
        cmp_line=line[0][1]
        
        if pre_cmp != cmp:
            if pre_cmp!="<@@>":
                strrp=str(pre_cmp)+" "+str(sigma_rule(pre_line))+'\n'
                output_file.write(strrp)
            lines_written += 1
            pre_cmp = cmp
            pre_line = cmp_line
        else :
            pre_line=join_baba(pre_line,line[0][1])

        if lines_written % Doc_id_Limit2 == 0 and pp!=lines_written:
            print(lines_written,end='\r')
            log_file.write(strrp)
            pp=lines_written
            output_file.close()
            file_num+=1
            output_file = open(output_path+"A"+str(file_num)+".txt", 'w')
            
    if pre_cmp!="<@@>":
        output_file.write(str(pre_cmp)+" "+str(sigma_rule(pre_line))+'\n')
        lines_written += 1
    return lines_written



