#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:54:55 2020

@author: gglj
"""


import pandas as pd
import matplotlib.pyplot as plt


attr = pd.read_csv('attr.txt',sep='\t',names=['linkid','length','direction','pathclass','speedclass','LaneNum','speedlimit','level','width'])


topo = pd.read_csv('topo.txt',sep='\t',names=['key','value'])
topo_dict = {}
for i in range(len(topo)):
    print(i)
    key = topo.iloc[i,0]
    value = list(map(int,topo.iloc[i,1].split(',')))
    topo_dict[key] = value
    

traffic = pd.read_csv('traffic/20190701.txt',sep=' |;',names=['link','label','current_slice_id','future_slice_id','recent_feature_1','recent_feature_2','recent_feature_3','recent_feature_4','recent_feature_5','history_feature_1_1','history_feature_1_2','history_feature_1_3','history_feature_1_4','history_feature_1_5','history_feature_2_1','history_feature_2_2','history_feature_2_3','history_feature_2_4','history_feature_2_5','history_feature_3_1','history_feature_3_2','history_feature_3_3','history_feature_3_4','history_feature_3_5','history_feature_4_1','history_feature_4_2','history_feature_4_3','history_feature_4_4','history_feature_4_5'])
print(traffic.loc[0])


attr_describe = attr.describe()
traffic_describe = traffic.describe()