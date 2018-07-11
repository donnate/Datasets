# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:20:59 2017

@author: cdonnat
"""
#### Extracts information from the ENRON dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

PATH_TO_DIR = '.../Enron/'
path_to_roles= PATH_TO_DIR+ 'roles_enron.txt'
handle_map=open(path_to_roles);
map_name2role={}
dict_role={}
it=0
for line in handle_map:
    line=line.strip("\n")
    lst=line.split("\t")
    if it<10:
        print lst
    email=lst[0].lower()
    rest=lst[1].split()
    print rest
    try:
        name=rest[0]+" "+rest[1]
        title=""
        for j in range(2,len(rest)):
            title+=rest[j]+" "
        title=title.rstrip(" ")
        print name
        map_name2role[name]=title
        try:
            dict_role[title].append(name)
        except:
            dict_role[title]=[]
            dict_role[title].append(name)
        print title
    except:
        pass
    it+=1


path_to_edges = PATH_TO_DIR +'data.txt'
handle_edges=open(path_to_edges);
edge_list=[]
for line in handle_edges:
    line=line.strip("\n")
    lst=line.split(" ")
    print len(lst)
    time=lst[0]
    src=lst[1]
    dest=lst[2]
    edge_list.append((src,dest))
import networkx as nx
Enron_graph=nx.from_edgelist(edge_list)
Enron_adj=nx.adjacency_matrix(Enron_graph).todense()

path_to_adj = PATH_TO_DIR+ 'data.txt'
handle_edges=open(path_to_adj);
edge_list=[]
it=0
N=184
titles=[]
for line in handle_edges:
    line=line.strip("\n")
    lst=line.split()
    print "length is:",len(lst)
    if it==0:
        print lst
        adj=pd.DataFrame(np.zeros((N,N)),index=lst[:-1])
        adj.columns=lst[:-1]
    else:
        print len(lst)
        print lst
        for i in range(N):
            adj.iloc[it-1,i]=int(lst[i+1])
        title=""
        for j in range(185,len(lst)):
            title+=lst[j]+" "
        title=title.rstrip(" ")   
        print title
        titles.append(title)
    it+=1
Graph_enron=nx.from_numpy_matrix(adj.as_matrix())
    