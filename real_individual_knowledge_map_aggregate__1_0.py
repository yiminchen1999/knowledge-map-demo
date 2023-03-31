# -*- coding: utf-8 -*-
"""Real_Individual_Knowledge_Map_Aggregate _1.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JISqAUi2TFgZBLD9ylm1iTWbgmZ-crZK
"""

# from palettable.colorbrewer.sequential import Blues_8
# palette_2021 = Blues_8.hex_colors

import pyvis
import pandas as pd
from pyvis.network import Network

palette_2021 = [['#e3342f', '#e8473f', '#ed5a4f', '#f26d5f', '#f7806f', '#fc937f', '#ffA68f', '#ffB99f'],
             ['#f6993f', '#f7a54f', '#f8b15f', '#f9bd6f', '#fac97f', '#fbd58f', '#fce19f', '#fdec6f'],
             ['#ffed4a', '#ffef5a', '#fff26a', '#fff57a', '#fff88a', '#fffb9a', '#fffeaa', '#ffffba'],
             ['#38c172', '#49c582', '#5aca92', '#6bcea2', '#7dd2b2', '#8fd6c2', '#a1dad2', '#b3dee2'],
             ['#4dc0b5', '#5ec4be', '#6fc8c7', '#80ccd0', '#91d0d9', '#a2d4e2', '#b3d8eb', '#c4dcf4'],
             ['#3490dc', '#4a94e0', '#5f98e4', '#74a0e8', '#89a8ec', '#9eb0f0', '#b3b8f4', '#c8c0f8'],
             ['#6574cd', '#7180d6', '#7d8cdf', '#8998e8', '#95a4f1', '#a1b0fa', '#adb6ff', '#b9bcff'],
             ['#9561e2', '#9f6de8', '#a979ee', '#b385f4', '#bd91fa', '#c79dff', '#d1a9ff', '#dbb5ff'],
             ['#f66d9b', '#f779a3', '#f885ab', '#f991b3', '#fa9dbb', '#fba9c3', '#fcb5cb', '#fdc1d3']]

# from palettable.colorbrewer.sequential import Blues_9
# palette_2022 = Blues_9.hex_colors
# palette_2022.reverse()
# palette_2022.append('#FAF6F0')

palette_2022 = [['#e3342f', '#e8473f', '#ed5a4f', '#f26d5f', '#f7806f', '#fc937f', '#ffA68f', '#ffB99f', '#ffccaf','#f7f7f7'],
             ['#f6993f', '#f7a54f', '#f8b15f', '#f9bd6f', '#fac97f', '#fbd58f', '#fce19f', '#fdec6f', '#fef89f','#f7f7f7'],
             ['#ffed4a', '#ffef5a', '#fff26a', '#fff57a', '#fff88a', '#fffb9a', '#fffeaa', '#ffffba', '#ffffca','#f7f7f7'],
             ['#38c172', '#49c582', '#5aca92', '#6bcea2', '#7dd2b2', '#8fd6c2', '#a1dad2', '#b3dee2', '#c5e2f2','#f7f7f7'],
             ['#4dc0b5', '#5ec4be', '#6fc8c7', '#80ccd0', '#91d0d9', '#a2d4e2', '#b3d8eb', '#c4dcf4', '#d5e0fd','#f7f7f7'],
             ['#3490dc', '#4a94e0', '#5f98e4', '#74a0e8', '#89a8ec', '#9eb0f0', '#b3b8f4', '#c8c0f8', '#ddc8fc','#f7f7f7'],
             ['#6574cd', '#7180d6', '#7d8cdf', '#8998e8', '#95a4f1', '#a1b0fa', '#adb6ff', '#b9bcff', '#c5c2ff','#f7f7f7'],
             ['#9561e2', '#9f6de8', '#a979ee', '#b385f4', '#bd91fa', '#c79dff', '#d1a9ff', '#dbb5ff', '#e5c1ff','#f7f7f7'],
             ['#f66d9b', '#f779a3', '#f885ab', '#f991b3', '#fa9dbb', '#fba9c3', '#fcb5cb', '#fdc1d3', '#fecddc','#f7f7f7']]

# from palettable.colorbrewer.sequential import Blues_5
# palette_2023 = Blues_5.hex_colors

palette_2023 = [['#e3342f', '#e8473f', '#ed5a4f', '#f26d5f', '#f7806f'],
             ['#f6993f', '#f7a54f', '#f8b15f', '#f9bd6f', '#fac97f'],
             ['#ffed4a', '#ffef5a', '#fff26a', '#fff57a', '#fff88a'],
             ['#38c172', '#49c582', '#5aca92', '#6bcea2', '#7dd2b2'],
             ['#4dc0b5', '#5ec4be', '#6fc8c7', '#80ccd0', '#91d0d9'],
             ['#3490dc', '#4a94e0', '#5f98e4', '#74a0e8', '#89a8ec'],
             ['#6574cd', '#7180d6', '#7d8cdf', '#8998e8', '#95a4f1'],
             ['#9561e2', '#9f6de8', '#a979ee', '#b385f4', '#bd91fa'],
             ['#f66d9b', '#f779a3', '#f885ab', '#f991b3', '#fa9dbb']]

keyword_category = pd.read_excel("assets/dictionary 2.0.xlsx",index_col=0).iloc[:,0:1]

file_names_2021 = ['Y2021_Student01','Y2021_Student02','Y2021_Student03','Y2021_Student04','Y2021_Student05','Y2021_Student06','Y2021_Student07']
year2021_df = []
for i in range(len(file_names_2021)):
    temp_df = pd.read_csv("assets/Year2021/"+file_names_2021[i]+".csv",index_col=0)
    year2021_df.append(temp_df)

file_names_2022 = ['Y2022_Student01','Y2022_Student02','Y2022_Student03','Y2022_Student04','Y2022_Student05','Y2022_Student06','Y2022_Student07','Y2022_Student08','Y2022_Student09','Y2022_Student10','Y2022_Student11','Y2022_Student12']
year2022_df = []
for i in range(len(file_names_2022)):
    temp_df = pd.read_csv("assets/Year2022/"+file_names_2022[i]+".csv",index_col=0)
    year2022_df.append(temp_df)

file_names_2023 = ['Y2023_Student01','Y2023_Student02','Y2023_Student03','Y2023_Student04','Y2023_Student05','Y2023_Student06','Y2023_Student07','Y2023_Student08','Y2023_Student09','Y2023_Student10','Y2023_Student11','Y2023_Student12']
year2023_df = []
for i in range(len(file_names_2023)):
    temp_df = pd.read_csv("assets/Year2023/"+file_names_2023[i]+".csv",index_col=0)
    year2023_df.append(temp_df)

keywords = list(year2021_df[0].head())

# the number shows which category the keyword belongs to
keywords_group = keyword_category.iloc[:, 0].to_numpy()

def aggregate_individual_knowledge_map(student_df, color_plate):
    nets = []
    for i in range(student_df.shape[0]):
        net = Network(notebook=True)#, heading="Individual Knowledge Map Aggregate Week " + str(i+1))
        occurence = student_df.iloc[:(i+1)].sum()
        for n in range(i+1): 
            for j, value in enumerate(student_df.iloc[n]):
                if value == 1:
                    category_number = keywords_group[j]-1
                    net.add_node(j, label=keywords[j], title='Week'+str(n+1),size=(int(occurence[j])+1)*3, color=color_plate[category_number][n])
        net_id = [dic['id'] for dic in net.nodes]
        for i in net_id:
            for j in net_id:
                if i != j and keywords_group[i] == keywords_group[j]:
                    net.add_edge(i,j,hidden=True)
        net.repulsion(central_gravity=1,spring_length=50)
        nets.append(net)
        
    return nets

indi_aggregate_s1_2021 = aggregate_individual_knowledge_map(year2021_df[0],palette_2021)
indi_aggregate_s2_2021 = aggregate_individual_knowledge_map(year2021_df[1],palette_2021)
indi_aggregate_s3_2021 = aggregate_individual_knowledge_map(year2021_df[2],palette_2021)
indi_aggregate_s4_2021 = aggregate_individual_knowledge_map(year2021_df[3],palette_2021)
indi_aggregate_s5_2021 = aggregate_individual_knowledge_map(year2021_df[4],palette_2021)
indi_aggregate_s6_2021 = aggregate_individual_knowledge_map(year2021_df[5],palette_2021)
indi_aggregate_s7_2021 = aggregate_individual_knowledge_map(year2021_df[6],palette_2021)

indi_aggregate_s1_2022 = aggregate_individual_knowledge_map(year2022_df[0],palette_2022)
indi_aggregate_s2_2022 = aggregate_individual_knowledge_map(year2022_df[1],palette_2022)
indi_aggregate_s3_2022 = aggregate_individual_knowledge_map(year2022_df[2],palette_2022)
indi_aggregate_s4_2022 = aggregate_individual_knowledge_map(year2022_df[3],palette_2022)
indi_aggregate_s5_2022 = aggregate_individual_knowledge_map(year2022_df[4],palette_2022)
indi_aggregate_s6_2022 = aggregate_individual_knowledge_map(year2022_df[5],palette_2022)
indi_aggregate_s7_2022 = aggregate_individual_knowledge_map(year2022_df[6],palette_2022)
indi_aggregate_s8_2022 = aggregate_individual_knowledge_map(year2022_df[7],palette_2022)
indi_aggregate_s9_2022 = aggregate_individual_knowledge_map(year2022_df[8],palette_2022)
indi_aggregate_s10_2022 = aggregate_individual_knowledge_map(year2022_df[9],palette_2022)
indi_aggregate_s11_2022 = aggregate_individual_knowledge_map(year2022_df[10],palette_2022)
indi_aggregate_s12_2022 = aggregate_individual_knowledge_map(year2022_df[11],palette_2022)

indi_aggregate_s1_2023 = aggregate_individual_knowledge_map(year2023_df[0],palette_2023)
indi_aggregate_s2_2023 = aggregate_individual_knowledge_map(year2023_df[1],palette_2023)
indi_aggregate_s3_2023 = aggregate_individual_knowledge_map(year2023_df[2],palette_2023)
indi_aggregate_s4_2023 = aggregate_individual_knowledge_map(year2023_df[3],palette_2023)
indi_aggregate_s5_2023 = aggregate_individual_knowledge_map(year2023_df[4],palette_2023)
indi_aggregate_s6_2023 = aggregate_individual_knowledge_map(year2023_df[5],palette_2023)
indi_aggregate_s7_2023 = aggregate_individual_knowledge_map(year2023_df[6],palette_2023)
indi_aggregate_s8_2023 = aggregate_individual_knowledge_map(year2023_df[7],palette_2023)
indi_aggregate_s9_2023 = aggregate_individual_knowledge_map(year2023_df[8],palette_2023)
indi_aggregate_s10_2023 = aggregate_individual_knowledge_map(year2023_df[9],palette_2023)
indi_aggregate_s11_2023 = aggregate_individual_knowledge_map(year2023_df[10],palette_2023)
indi_aggregate_s12_2023 = aggregate_individual_knowledge_map(year2023_df[11],palette_2023)



indi_aggregate_s7_2021[7].show("assets/2021_s7_aggregate_8.html")

indi_aggregate_s6_2021[7].show("assets/2021_s6_aggregate_8.html")

indi_aggregate_s5_2021[7].show("assets/2021_s5_aggregate_8.html")

indi_aggregate_s4_2021[7].show("assets/2021_s4_aggregate_8.html")

indi_aggregate_s3_2021[7].show("assets/2021_s3_aggregate_8.html")

indi_aggregate_s2_2021[7].show("assets/2021_s2_aggregate_8.html")

indi_aggregate_s1_2021[7].show("assets/2021_s1_aggregate_8.html")







