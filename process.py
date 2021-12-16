import csv

rawdata=[]
with open("D:/Desktop/a/data",encoding="utf-8") as file:
    rawdata=eval(file.read())

trans=[]

with open("D:/Desktop/a/translate.csv",encoding="utf-8") as file:
    trans = list(csv.reader(file))

def replace(x):
    for i in trans:
        if x in i:
            return i[0]

data=[[],[],[],[]]

title=rawdata[0].pop(0)
title[0]="货币"

#ccb
data[0]=[[i[0],str(round(float(i[1])*100,2)),str(round(float(i[2])*100,2))] for i in rawdata[0]]
#icbc
data[1]=[[i[0],i[1],i[3]] for i in rawdata[1]]
#abc
data[2]=[[i[0],i[2],i[3]] for i in rawdata[2]]
#boc
data[3]=[[i[0],i[1],i[3]] for i in rawdata[3]]

for i,j in zip(range(len(data)),data):
    for k,l in zip(range(len(j)),j):
        data[i][k][0]=replace(l[0])



title=["Type","Bid","Offer"]

with open("D:/Desktop/a/result.csv","w",encoding="utf-8",newline="") as file:
    w = csv.writer(file)

    w.writerow(title)

    for i,j in zip([["ccb"],["icbc"],["abc"],["boc"]],data):

        w.writerow(i)
        w.writerows(j)

        
with open("D:/Desktop/a/data2","w",encoding="utf-8") as file:
    file.write(str(data))