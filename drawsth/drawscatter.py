# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:04:31 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""


import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.lines as mlines
from matplotlib.legend import Legend
#plt.style.use('ggplot')

def drawscatter(ax,xs,ys,**ks):
    markers = ['o', 'v', '^', '<', '>', 'D', 's', 'P']
    for x,y,m in zip(xs,ys,markers):
        ax.scatter(x,y,marker=m,**ks)



if '__main__'==__name__:
    df = pd.read_excel(r"***")
    label = df.pop('target')
    label = [x[3:] for x in label]
    cols = df.columns
    markers = ['o', 'v', '^', '<', '>', 'D', 's', 'P']
    
    f,ax = plt.subplots(figsize=(10,10))
#    f.set_facecolor('blueviolet')
#    ax.grid(zorder=-10000)
    
    colors = [
            '#eb397a','#6c8df4','#55d14a','#eeda5a'
              ]
    for n,color in zip(range(0,8,2), colors):
        drawscatter(ax,df.iloc[:,n+1], df.iloc[:,n],color=color,s=80,alpha=1)

    ax.plot([0,1],[0,1],linestyle='--',c='gray')
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_yticklabels([None,0.2,0.4,0.6,0.8,1.0])
    ax.set_xticklabels([0,0.2,0.4,0.6,0.8,1.0])
    ax.tick_params(direction='in', which='both', labelsize=18)
    ax.set_xlabel('$\mathregular{AUC_{original}}$',fontdict={'family':'arial', 'size':26})
    ax.set_ylabel('$\mathregular{AUC_{training}}$',fontdict={'family':'arial', 'size':26})
    
    
    ##########################################legend##########################################      
    legend_1 = [mlines.Line2D([0], [0], color=colors[0], marker=m, linestyle='None', 
                      markersize=10) for m in markers]
    leg_1 = Legend(ax, legend_1, labels=label, loc=4)
    
    legend_2 = [mlines.Line2D([0], [0], color=c, marker='o', linestyle='None', 
                          markersize=10) for c in colors]
    leg_2 = Legend(ax, legend_2, labels=cols[0::2], loc=2)
    
    ax.add_artist(leg_1)
    ax.add_artist(leg_2)
    ##########################################legend##########################################
    
    ax.set_axisbelow(True)
    ax.grid()
    
    plt.savefig('demo.pdf')
    
    
    
    
    
    
    
    
    
    
    
    
    
    