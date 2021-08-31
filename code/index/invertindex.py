from config import *

inv_dic={}
#  title info catty extlinlk refer body

def deal_with_dump(id,dump):
    dic={}
    for i in range(len(dump)):
        if i != 0:
            tok=dump[i]
            for x in tok:
                # if len(x) > 3:
                if x not in dic:
                    dic[x]=[0,0,0,0,0,0]
                dic[x][i-1]=1
    merge_with_global(id,dic)

def merge_with_global(id,dic):
    for x in dic:
        if x not in inv_dic:
            inv_dic[x]=[[],[],[],[],[],[]]
        for i in range(len(dic[x])):
            if dic[x][i] > 0:
                inv_dic[x][i].append(id)

def give_me_final_dump(path):
    stat2=0
    file_name = str(path)+"/inv/"+str(2)+".txt"
    fp=open(file_name,"w")
    # for x in inv_dic:
    for x in sorted(inv_dic.keys()):
        aa=""
        for i in inv_dic[x]:
            aa+=((",").join(i))+";"
        print(str(x)+" "+str(aa),file=fp)
        stat2+=1
    fp.close()
    return stat2

def doc_id_to_file_name(doc_id):
    file_id=doc_id/Doc_id_Limit

def write_title(path,a,file_id):
    file_name = str(path)+"/titles/"+str(file_id)+".txt"
    fp=open(file_name,"w")
    for x in a:
        print(str(x[0])+"<@>"+str(x[1]),file=fp)

def tit_by_doc_id(path,doc_id):
    file_id=doc_id//Doc_id_Limit
    file_name = str(path)+"/titles/"+str(file_id)+".txt"
    line_number = doc_id%Doc_id_Limit
    fp=open(file_name)
    for i, line in enumerate(fp):
        if i == line_number:
            line=line.split("<@>")[1]
            break
    fp.close()
    return line

