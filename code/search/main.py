import sys

n=len(sys.argv)
if n != 3:
    print("Improper argument passed")
else:
    code_file,invert_path,query_string = sys.argv
    print("search")
    print(invert_path)
    print(query_string)