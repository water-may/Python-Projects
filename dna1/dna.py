import sys
import csv

def main():
    l = 0
    if len(sys.argv) != 3:
        print("Invalid Use")
        sys.exit(1)
    dic =  open(sys.argv[1], 'r')
    sfile = open(sys.argv[2], 'r')
    seq = sfile.read()

    values = {"SATname":[], "SATlen":[]}

    for line in dic:
        if line.startswith('name'):
            SATs = line.split(",")
    # load values
    SATs.remove('name')
    for sat in SATs:
        sat = sat.rstrip()
        c = count(sat, seq)
        values["SATname"].append(sat)
        values["SATlen"].append(c)
        l += 1
        # print(values)

    # Check
    check(values, l)
            

def count(asat, seq):
    leng  = len(seq)
    slen = len(asat)
    count = c = 0
    for i in range(0, leng - slen, 1):
        sat = ""
        for j in range(i, i + slen, 1):
            sat += seq[j]
        if sat == asat:
            c += 1
            s = "" 
            # print(sat)
            for k in range(i+slen, i+(2 * slen), 1):
                s += seq[k]
            # print("<" + s + ">")
            if s != sat:
                if c > count:
                    count = c
                    c = 0
                else:
                    c = 0
            # print(str(c))
            # print(str(count))
    return count        
               
def check(values, l):
    dic = open(sys.argv[1])
    
    c = 0
    s = 0
    # print(len(values['SATname']))
    # print(values['SATname'])
    for line in dic:
        if line.startswith('name'):
                continue
        else:
            all = line.split(',')

        i = 1
        c = 0
        for value in values['SATlen']:
            # print(value)
            # print("all: " + all[i])
            if value == int(all[i]):
                c += 1
            i += 1
            # print("c: " + str(c))

            
        if (c == l):
            print(all[0])
            s += 1
    if s != 1:
        print("No match")   

main()
