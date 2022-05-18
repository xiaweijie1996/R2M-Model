# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:39:19 2022

@author: WeijieXia
"""

import pandas as pd


"The parameters you can change"
"————————————————————————————————————————————"

day = [[0.1,0.1,0.1,0.7]]

week = [[0.1,0.1,0.1,0.7],
        [0.1,0.2,0.1,0.6],
        [0.1,0.1,0.1,0.7],
        [0.1,0.1,0.1,0.7],
        [0.1,0.1,0.1,0.7],
        [0.1,0.1,0.1,0.7],
        [0.1,0.1,0.1,0.7]]

option = 'Week' # Week or Day

"————————————————————————————————————————————"

day = pd.DataFrame(day)
week = pd.DataFrame(week)

file = pd.DataFrame([])

if option == 'Week':
    for z in range(int(8760/7)):
        file = pd.concat([file,week],axis=0)
    file = pd.concat([file,week.iloc[:3,:]])
    
if option == 'Day':
    for z in range(int(8760)):
        file = pd.concat([file,day],axis=0)

 
file.to_csv('Pv_split.csv')