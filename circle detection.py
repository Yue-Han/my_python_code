# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:35:44 2013

@author: YueHan
"""

import networkx as nx
import csv
from datetime import datetime

def drawedge(treeid):
    data = csv.reader(open('D:/network/clean/'+str(treeid)+'.csv','r'))
    data = sorted(data, key = lambda row: row[0])
    
    G = nx.DiGraph()
    
    def addnode(x,y):
        G.add_weighted_edges_from([(str(x),str(y),1)])
    
    lines=[]  
    for rows in data:
        lines.append(rows[0])
    for i in range(1,len(lines)):
        x = data[i][1]
        y = data[i][2]
        a = addnode(x,y)
    
    nx.simple_cycles(G)
    sc = str(nx.simple_cycles(G))
    u = '[]'
    if sc!= u:
        fc = open('D:/network/cycle detection/'+str(treeid)+'.txt','w')
        fc.write(sc)
        fc.close()
    
reads=[]
r = csv.reader(open('D:/daily/remixes/allclean.csv'))
for rows in r:
    reads.append(rows[0])

for i in range(1,len(reads)):
    treeid=reads[i]
    try:
        a=drawedge(treeid)
    except Exception:
        pass
    print i