import matplotlib.pyplot as plt


with open('data2',encoding="utf-8") as file:

    data = eval(file.read())

plotdata=[]

for i in data:
    tmp=[]
    
    for j,k,l in i:

        if k!="" and l!="":

            tmp.append([j,float(k),float(l)])
    plotdata.append(tmp)


plotdata=[list(zip(*x)) for x in plotdata]


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)


plots=[ax1, ax2, ax3, ax4]
banks=["CCB","ICBC","ABC","BOC"]



for i,j,k in zip(plots,range(4),banks):

    i.set_xlabel(k)
    i.set_ylabel("Exchange Rate")

    i.set_title("Bid")
    
    i.bar(plotdata[j][0],plotdata[j][1])



plt.show()

