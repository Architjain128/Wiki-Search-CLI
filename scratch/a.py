# parse a txt file in .csv format
def parse(path):
    with open(path) as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            print(line.split('>'))
        
a=input()
parse(a)