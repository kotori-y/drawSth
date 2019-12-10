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
from load import load
from itertools import cycle
#plt.style.use('ggplot')


def drawscatter(ax,xs,ys,**ks):
    markers = ['o', 'v', '^', '<', '>', 'D', 's', 'P']
    for x,y,m in zip(xs,ys,markers):
        ax.scatter(x,y,marker=m,**ks)


def main(file,target_field='Target',save_dir=None):
    df = load(file)
    targets = df.pop(target_field)
    scores = df.columns
    num = len(scores)
    
    markers = ['o', 'v', '^', '<', '>', 'D', 's', 'P']
    colors = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3',
              '#fdb462','#b3de69','#fccde5','#d9d9d9','#bc80bd']
              
    f,ax = plt.subplots(figsize=(5,5))
    for n,color in zip(range(0,num,2), colors):
        drawscatter(ax,df.iloc[:,n], df.iloc[:,n+1],color=color,s=40,alpha=1)
    
    ax.plot([0,1],[0,1],linestyle='--',c='gray')
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['right'].set_linewidth(0.5)
    ax.spines['top'].set_linewidth(0.5)
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_yticklabels([None,0.2,0.4,0.6,0.8,1.0],fontdict={'family': 'arial', 'size':10})
    ax.set_xticklabels([0,0.2,0.4,0.6,0.8,1.0],fontdict={'family': 'arial', 'size':10})
    ax.set_xlabel('AUC Classical SFs',fontdict={'family': 'arial', 'size':10})
    ax.set_ylabel('AUC EATL SFs',fontdict={'family': 'arial', 'size':10})
    ax.tick_params(direction='in', which='both', labelsize=10)
    
    ##########################################legend##########################################      
    legend_1 = [mlines.Line2D([0], [0], color=colors[0], marker=m, linestyle='None', 
                      markersize=9) for m in markers]
    
    leg_1 = Legend(ax, legend_1, labels=targets, ncol=2, 
                   bbox_to_anchor=(0.49, .505), 
                   prop={'family': 'arial','size':9})
    
    legend_2 = [mlines.Line2D([0], [0], color=c, marker='o', linestyle='None', 
                          markersize=9) for c in colors]
    
    leg_2 = Legend(ax, legend_2, labels=scores[0::2], ncol=2, 
                   loc=4, 
                   prop={'family': 'arial','size':9})
    
    ax.add_artist(leg_1)
    ax.add_artist(leg_2)
    ##########################################legend##########################################
    
    if save_dir:
        plt.savefig(save_dir,bbox_inches='tight')
    else:
        pass
    plt.show()
    
    
if '__main__'==__name__:
    main(r"C:\Users\0720\Desktop\MATE\xgl\1101scatter.xlsx",save_dir=r'C:\Users\0720\Desktop\MATE\yzy\mc\s1102.pdf')
#    df = pd.read_excel(r"C:\Users\0720\Desktop\MATE\xgl\Scatter_plot_GOLD.xlsx")
#    label = df.pop('target')
#    label = [x[3:] for x in label]
#    cols = df.columns
#    markers = ['o', 'v', '^', '<', '>', 'D', 's', 'P']
#    
#    f,ax = plt.subplots(figsize=(10,10))
##    f.set_facecolor('blueviolet')
##    ax.grid(zorder=-10000)
#    
#    colors = [
#            '#eb397a','#6c8df4','#55d14a','#eeda5a', '#800000'
#              ]
#    for n,color in zip(range(0,8,2), colors):
#        drawscatter(ax,df.iloc[:,n+1], df.iloc[:,n],color=color,s=80,alpha=1)
#
#    ax.plot([0,1],[0,1],linestyle='--',c='gray')
#    ax.spines['bottom'].set_linewidth(2)
#    ax.spines['left'].set_linewidth(2)
#    ax.spines['right'].set_linewidth(2)
#    ax.spines['top'].set_linewidth(2)
#    ax.set_xlim([0,1])
#    ax.set_ylim([0,1])
#    ax.set_yticklabels([None,0.2,0.4,0.6,0.8,1.0])
#    ax.set_xticklabels([0,0.2,0.4,0.6,0.8,1.0])
#    ax.tick_params(direction='in', which='both', labelsize=18)
##    ax.set_xlabel('$\mathregular{auc_{Score-MOE}}$',fontdict={'family':'arial', 'size':26, 'fontstyle':'italic'})
##    ax.set_ylabel('$\mathregular{AUC_{training}}$',fontdict={'family':'arial', 'size':26})
#    ax.text(0.37, -0.09, 'auc', fontdict={'family':'arial', 'size':26, 'fontstyle':'italic'})
#    ax.text(0.46, -0.09, 'Score-GOLD', fontdict={'family':'arial', 'size':26})
#    
#    ax.text(-0.11, 0.41, 'auc', fontdict={'family':'arial', 'size':26, 'fontstyle':'italic', 'rotation':'vertical'})
#    ax.text(-0.11, 0.55, 'EATL', fontdict={'family':'arial', 'size':26, 'rotation':'vertical'})
#    
#    
#    ##########################################legend##########################################      
#    legend_1 = [mlines.Line2D([0], [0], color=colors[0], marker=m, linestyle='None', 
#                      markersize=10) for m in markers]
#    leg_1 = Legend(ax, legend_1, labels=label, loc=4)
#    
#    legend_2 = [mlines.Line2D([0], [0], color=c, marker='o', linestyle='None', 
#                          markersize=10) for c in colors]
#    leg_2 = Legend(ax, legend_2, labels=cols[0::2], loc=2)
#    
#    ax.add_artist(leg_1)
#    ax.add_artist(leg_2)
#    ##########################################legend##########################################
#    
#    ax.set_axisbelow(True)
#    ax.grid()
#    
#    plt.savefig('GOLD_score.pdf')
#    
#    
    
    
    
    
    
    
    
    
    
    
    
    