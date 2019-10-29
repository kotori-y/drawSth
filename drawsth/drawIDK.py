# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:38:29 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
#from itertools import product


def draw(file):  
    df = pd.read_csv(file)  
    colors = ['#ce9f9f','#bbc7d4','#aec5a2','#e4bcfb','#f9f0f0',
             '#6bc5c6','#f7911f','#e42f68','#f98dbe','#76c158',
             '#b7e6ea','#f4bfb0','#f2d4a6','#ffaf8c','#2cc0c5',
             '#000000','#4d88ec']
    
    
    f,ax = plt.subplots(figsize=(15,15*0.618))
    for rows,color in zip(df.iterrows(),colors):
#        idx = rows[0]+1
        row = rows[-1]
        ax.scatter(range(1,15),list(row),s=80,color=color)
        ax.plot(range(1,15),list(row),color=color,lw=3,alpha=0.4)
    
    ax.set_xticks(range(1,15))
    ax.set_xticklabels(df.columns,rotation=30)
    ax.tick_params(direction='in',which='both',labelsize=20,length=7,width=4,right=True,top=True)
    ax.set_ylabel('Enrichment Factor(%)',fontdict={'size':28},labelpad=15)
    ax.spines['bottom'].set_linewidth(4)
    ax.spines['left'].set_linewidth(4)
    ax.spines['right'].set_linewidth(4)
    ax.spines['top'].set_linewidth(4)
#    plt.savefig('{}.pdf'.format(file.replace('.csv','')))
    
    
if '__main__'==__name__:
    os.chdir(r'C:\Users\0720\Desktop\MATE\akuma')
    files = os.listdir()
    for file in files:
        draw(file)