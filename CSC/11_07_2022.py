import csv

fh = open('sample_001.csv' , 'w')
'''
l = '12A01' , 'ANISH' , 'CS'

l1 = [
    [1,2,3,4],
    ['a','b'],
    [12.56,12.756]
    ]
obj = csv.writer(fh , delimiter = 's')
obj.writerows(l1)
'''
robj = csv.reader(fh , delimiter = ',')
for i in robj:
    print(i)

fh.close()
