
import networkx as nx
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import os
import errno
import time

def drawremixtreenew(treeid):
    
    data = csv.reader(open('/Users/yuehan/Desktop/demo analysis/'+str(treeid)+'/'+str(treeid)+'color.csv','r'))
    for rows in data:
        times.append(rows[2])
        projects.append(rows[0])
        parents.append(rows[3])
        users.append(rows[1])
        colors.append(rows[4])
    
    utest=[]
    uduplicates=[]
    for i in range(0,len(users)):
        if users[i] in utest:
            uduplicates.append(users[i])
        else:
            utest.append(users[i])
    
    for i in range(0,len(users)):
        if users[i] in uduplicates:
            recolors.append(colors[i])
        else:
            recolors.append("#848482")
    
    with open('/Users/yuehan/Desktop/demo analysis/'+str(treeid)+'/'+str(treeid)+'clean.csv','wb') as f1:
        w = csv.writer(f1)
        for i in range(1,len(times)):
            sharetime=times[i]
            project=projects[i]
            parent=parents[i]
            user=users[i]
            color=recolors[i]
            w.writerow([sharetime,project,parent,user,color])
    
    data2 = csv.reader(open('/Users/yuehan/Desktop/demo analysis/'+str(treeid)+'/'+str(treeid)+'clean.csv','r'))
    data2 = sorted(data2, key = lambda row: row[0])
    
    newprojects=[]
    newusers=[]
    newcolors=[]
    
    for rows in data2:
        newprojects.append(rows[1])
        newusers.append(rows[3])
        newcolors.append(rows[4])
    
    newpath = r"/Users/yuehan/Desktop/demo analysis/"+str(treeid)+"/comics/"
    if not os.path.exists(newpath): os.makedirs(newpath)
    
    G = nx.Graph()
    G.add_node(data2[0][1])
    
    order=G.nodes()
    
    udict={}
    udict['null']='null'
    for j in range(0,len(newusers)):
        udict[newprojects[j]]=newusers[j]+'/'+newprojects[j]
    
    labels={}
    for v in range(0,len(order)):
        labels[order[v]]=udict[order[v]]
    
    
    
    cdict={}
    cdict['null']="#848482"
    for v in range(0,len(newcolors)):
        cdict[newprojects[v]]= newcolors[v]
    
    cols=[]
    for v in range(0,len(order)):
        cols.append(cdict[order[v]])
    
    
    pos=nx.spring_layout(G)
    nx.draw(G,cmap=pos,node_color= [z for z in cols],node_size=15,with_labels=False)
    nx.draw_networkx_labels(G,pos,labels,font_size=5)
    
    
    plt.savefig("/Users/yuehan/Desktop/demo analysis/"+str(treeid)+"/comics/"+"/0.png", dpi=500)
    plt.clf()
    
    def addnode(x,y,num):
        G.add_edge(str(x),str(y))
        
        order=G.nodes()
        
        labels={}
        for v in range(0,len(order)):
            labels[order[v]]=udict[order[v]]
        
        cols=[]
        for v in range(0,len(order)):
            cols.append(cdict[order[v]])
        
        pos=nx.spring_layout(G)
        nx.draw(G,pos,node_color= [z for z in cols],node_size=40,linewidths=0,width=0.3,with_labels=False)
        nx.draw_networkx_labels(G,pos,labels,font_size=2)
        plt.savefig("/Users/yuehan/Desktop/demo analysis/"+str(treeid)+"/comics/"+str(num)+".png", dpi=500)
        plt.clf()
    
    lines=[]
    for rows in data2:
        lines.append(rows[0])
    for i in range(1,len(lines)):
        x = data2[i][1]
        y = data2[i][2]
        if y in newprojects:
            num=i
        else:
            udict[y]='noinfo'
            cdict[y]="#848482"            
            num=i
        b=addnode(x,y,num)
        print i



times=[]
projects=[]
parents=[]
colors=[]
recolors=[]
users=[]     
project= input('projectid is:')
drawremixtreenew(project)

