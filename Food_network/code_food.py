# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:59:21 2017

@author: cdonnat
"""

import numpy as np


path_to_map='../Food_network/scirep-cuisines-detail/map.txt'
handle_map=open(path_to_map);
map_cuisine={}
for line in handle_map:
    line=lst=line.strip("\n")
    lst=line.split("\t")
    map_cuisine[lst[0]]=lst[1]
    
path_to_food='../Food_network/ingr_comp/ingr_info.tsv'
handle_food=open(path_to_food);
food={}
category={}
it_category=0
it=0
for line in handle_food:
    if it>0:
        line=lst=line.strip("\n")
        lst=line.split("\t")
        try:
            cat=category[lst[2]][0]
            category[lst[2]][1]+=1
        except:
            it_category+=1
            category[lst[2]]=[it_category,1]
            cat=it_category
        food[lst[1]]=(int(lst[0]),lst[2],cat)
        
    it+=1
    
    
    
path_to_att='../Food_network/scirep-cuisines-detail/epic_recipes.txt'
it=0
recipes={}
label_region=[]
regions={}
handle=open(path_to_att);
line_count=0
region_count=0
stock={}

line_count=0
for line in handle:
    #if line_count<nb_stocks:
        line=lst=line.strip("\n")
        lst=line.split("\t")
        recipes[line_count]=lst[1:]
        reg=lst[0].lower()
        print(reg)
        try:
            lab=regions[reg]
        except:
            region_count+=1
            regions[reg]=region_count
            lab=region_count 
        label_region[line_count]=lab
        #print content
        line_count+=1
        
path_to_menu='../Food_network/scirep-cuisines-detail/menu_recipes.txt'       
for line in handle:
    #if line_count<nb_stocks:
        line=lst=line.strip("\n")
        lst=line.split("\t")
        recipes[line_count]=lst[1:]
        reg.lower()=lst[0]
        try:
            lab=regions[reg]
        except:
            region_count+=1
            regions[reg]=region_count
            lab=region_count 
        label_region[line_count]=lab
        #print content
        line_count+=1
