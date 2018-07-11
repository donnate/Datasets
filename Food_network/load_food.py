# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:59:21 2017

@author: cdonnat
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv




path_to_map='../Food_network/scirep-cuisines-detail/map.txt'
handle_map=open(path_to_map);
map_cuisine={}
it=0
for line in handle_map:
    line=lst=line.strip("\n")
    lst=line.split("\t")
    reg=lst[0].lower()
    #reg=reg.replace("-","")
    map_cuisine[reg]=lst[1]
    #map_cuisine[reg][1]=it
    it+=1
map_cuisine2={}
map_cuisine2 ["china"]="chinese" 
map_cuisine2 ["easterneuropean_russian"]="easterneuropean" 
map_cuisine2 ["france"]="french" 
map_cuisine2 ["germany"]="german"
map_cuisine2 ["india"]="indian"
map_cuisine2 ["italy"]="italian"
map_cuisine2 ["japan"]="japanese"
map_cuisine2 ["korea"]="korean"
map_cuisine2 ["mexico"]="mexican"
map_cuisine2 ["scandinavia"]="scandinavian"
map_cuisine2 ["spain"]="spanish_portuguese"
map_cuisine2 ["portugal"]="spanish_portuguese"
map_cuisine2 ["LatinAmerican"]="central_southamerican"
map_cuisine2 ["south-america"]="central_southamerican"
map_cuisine2 ["thailand"]="thai"
map_cuisine2 ["uk-and-ireland"]="english_scottish"
map_cuisine2 ["vietnam"]="vietnamese"


    
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
            lab=regions[reg][0]
            regions[reg][1]+=1
        except:
            region_count+=1
            regions[reg]=[region_count,1]
            lab=region_count
        label_region.append(lab)
        #print content
        line_count+=1
        
path_to_menu='../Food_network/scirep-cuisines-detail/menu_recipes.txt'   
handle_menu=open(path_to_menu);  
for line in handle_menu:
    
    #if line_count<nb_stocks:
        line=lst=line.strip("\n")
        lst=line.split("\t")
        recipes[line_count]=lst[1:]
        reg=lst[0].lower()
        if (reg in map_cuisine2.keys()):
            reg=map_cuisine2[reg]
        print reg
        try:
            lab=regions[reg][0]
            regions[reg][1]+=1
        except:
            region_count+=1
            regions[reg]=[region_count,1]
            lab=region_count
        label_region.append(lab)
        #print content
        line_count+=1
        
path_to_allr='../Food_network/scirep-cuisines-detail/allr_recipes.txt'   
handle_allr=open(path_to_allr);  
for line in handle_allr:
    
    #if line_count<nb_stocks:
        line=lst=line.strip("\n")
        lst=line.split("\t")
        recipes[line_count]=lst[1:]
        reg=lst[0].lower()
        if (reg in map_cuisine2.keys()):
            reg=map_cuisine2[reg]
        print reg
        try:
            lab=regions[reg][0]
            regions[reg][1]+=1
        except:
            region_count+=1
            regions[reg]=[region_count,1]
            lab=region_count
        label_region.append(lab)
        #print content
        line_count+=1
        
        
### make the graphs per country
Graphs={}
for key in regions.keys():
    A=np.zeros((len(food),len(food)))
    key_id=regions[key][0]
    id_recipe=[e for e in range(len(label_region)) if label_region[e]==key_id]
    l=len(id_recipe)
    print(l)    
    for e in id_recipe:
        recette=recipes[e]
        try:
            ingredients=[food[ing][0] for ing in recette]
            for ing in ingredients:
                A[ing, ingredients]=A[ing, ingredients]+np.ones(len(ingredients))
        except:
            print "ingredient not listed"
    Graphs[key]=1.0/l*A ## divide by the volume


def plot_heat_map(country):    
    row_sum=np.sum(Graphs[country],1)
    food_used=[e for e in range(len(food)) if row_sum[e]>0]
    res_graph=np.zeros((len(food_used),len(food_used)))
    it=0
    while it<len(food_used):
        res_graph[it,:]=Graphs[country][food_used[it],food_used]
        it+=1
    fig=plt.figure()
    plt.imshow(regions[country][1]*res_graph, cmap='hot')
    plt.show()
    fig.savefig("food_used_"+country+".png")
    return("done")


write_csv=False
if write_csv==True:
    key_it=0
    for key in regions.keys():
        key_it=regions[key][0]
        file_dest='../Food_network/Graphs/grph_file'+str(key_it)+'.csv'
        with open(file_dest, 'w') as csvfile:
            writer = csv.writer(csvfile)
            [writer.writerow(r) for r in Graphs[key]]   
    file_dest='../Food_network/Graphs/food_map.csv'
    with open(file_dest, 'w') as csvfile:
            writer = csv.writer(csvfile)
            [writer.writerow([k,food[k][0],food[k][1]]) for k in food.keys()] 
            
    file_dest='../Food_network/Graphs/keys_graphs.csv'
    with open(file_dest, 'w') as csvfile:
            writer = csv.writer(csvfile)
            [writer.writerow([k,regions[k][0]]) for k in regions.keys()]        
            

            
            
            