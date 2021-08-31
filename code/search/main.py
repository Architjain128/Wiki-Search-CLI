import sys
from magic import *

n=len(sys.argv)
if n != 3:
    print("Improper argument passed"+str(sys.argv)+str(n))
else:
    code_file,invert_path,query_string = sys.argv
    print("search")
    print(invert_path)
    print(query_string)
    posting_list=[]
    posting_list+=find_query(invert_path,query_string.lower())
    
    if posting_list == []:
        print("No results found")
    else:
        for i in posting_list:
            print(">>"+i)