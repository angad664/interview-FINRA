#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: angadsingh
"""

import pandas as pd
df = pd.read_excel('movie.xlsx')
#print (df.head())
dt_act  =list()
dt_fin = dict()
for key, value in df.iteritems():
    #print(key)
    if key!='Movie':
        #print (type(value))
        dt_act = value.tolist()

for each in dt_act:
    if each in dt_fin.keys():
        dt_fin[each] +=1
    else:
        dt_fin[each] = 1

sorted_dt_fin = sorted(dt_fin.items(), key=lambda kv: kv[1])
#print (list(dict(sorted_dt_fin).keys()))
print (sorted_dt_fin[::-1][:10])
#print ("The most popular actor is " +list(dt_fin.keys())[0])
