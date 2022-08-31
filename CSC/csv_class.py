'''
import csv
a=open("inp1.csv","w")
l=[[1201,"anish","cs"],[1204,"kaveen","bio"]]
wob=csv.writer(a,delimiter="k")
wob.writerows(l)
a.close()


with open("inp1.csv","r" , newline = '\n') as a:
    ro=csv.reader(a,delimiter="e")
    for i in ro:
        print(i)
'''

import sys

sys.stdout.write('Hello Sv \n')
sys.stderr.write('Sv rocks !')

