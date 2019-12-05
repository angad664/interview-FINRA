#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: angadsingh
"""

games = ["PM","SR","PIU","SI","MB","MK","ATB","ST","SW","SFII"]
completion_time = [75,45,30,35,30,15,60,90,20,10]
payout_rate = [250,280,150,120,200,100,300,350,110,90]
ratio = list()
ratio_dict = dict()
total_time = 120
for each in range(len(payout_rate)):
    ratio.append(payout_rate[each]/completion_time[each])

for i,j in enumerate(ratio):
    ratio_dict[i] = j

sorted_dt_fin = sorted(ratio_dict.items(), key=lambda kv: kv[1])
sorted_dt_fin = sorted_dt_fin[::-1]
#print ((sorted_dt_fin))
temp_time = 0
i = 0
total = 0
final_list = list()
while temp_time <= 120 and i < len(sorted_dt_fin):

    diff = total_time - temp_time
    if completion_time[sorted_dt_fin[i][0]] <= diff:
        #print (sorted_dt_fin[i][0])
        total += payout_rate[sorted_dt_fin[i][0]]
        final_list.append(games[sorted_dt_fin[i][0]])
        temp_time += completion_time[sorted_dt_fin[i][0]]
    i +=1

print ('The order is : '  +'-->'.join(final_list) )
print(temp_time)
print(total) # total amount
