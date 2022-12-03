import sys
import csv

def main():
    dictonary = open(sys.argv[1])
    sfile = open(sys.argv[2], 'r')
    seq = sfile.read()
    AGAT, AATG, TATC = count(seq)
    vaid(AGAT, AATG, TATC, dictonary)
    print("AGAT: " + str(AGAT) + "\nAATG: " + str(AATG) + "\nTATC: " + str(TATC))
    sfile.close()

def count(seq):
    leng = len(seq)
    ag = aa = ta = 0
    AGAT = AATG = TATC = 0
    for i in range(0, leng - 4, 1):
        set = ""
        for j in range(i, i+4, 1):
            set += seq[j]
        print(set)
        if set == "AGAT":
            ag += 1
            s = ""
            for k in range(i+4, i+8, 1):
                s += seq[k]
            print("<" + s + ">")
            if s != "AGAT":
                if ag > AGAT:
                    AGAT = ag
                    ag = 0
                elif ag <= AGAT:
                    ag = 0
        elif set == "AATG":
            aa += 1
            s = ""
            for k in range(i+4, i+8, 1):
                s += seq[k]
            print("<" + s + ">")
            if s != "AATG":
                if aa > AATG:
                    AATG = aa
                    aa = 0
                elif aa <= AATG:
                    aa = 0
        elif set == "TATC":
            ta += 1
            s = ""
            for k in range(i+4, i+8, 1):
                s += seq[k]
            print("<" + s + ">")
            if s != "TATC":
                if ta > TATC:
                    TATC = ta
                    ta = 0
                elif ta <= TATC:
                    ta = 0
    return AGAT, AATG, TATC

def valid(AGAT, AATG, TATC), dic):
     reader = csv.DictReader
    
main()


