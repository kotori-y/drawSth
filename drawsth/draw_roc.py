# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:28:09 2019

@Author: Zhi-Jiang Yang, Guo-Li Xiong
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; xgl150327@csu.edu.cn
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

from load import load
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


def draw_roc(file, label_col, Ascore_col, Dscore_col,figsize=(5,5)):
    data = load(file)
    score_col = Ascore_col+Dscore_col 
    font_kws = {'family':'arial','size':18}
    f,ax = plt.subplots(figsize=figsize) 
    ax.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Random')
    label = data.pop(label_col)
    for col in score_col:
        score = data[col]
        if col in Ascore_col:
            pos_label = 0
        else:
            pos_label = 1 
        fpr, tpr, _= roc_curve(label, score, pos_label=pos_label)
        AUC = auc(fpr,tpr)  
        ax.plot(fpr,tpr,linewidth=1.5,label=col+' (auc=%.3f)'%AUC)
    ax.set_xlabel('false positive rate', fontdict=font_kws)
    ax.set_ylabel('true positive rate', fontdict=font_kws)
    ax.set_ylim([0.0,1.0])
    ax.set_xlim([0.0,1.0])
    ax.tick_params(direction='in', which='both', labelsize=12)
    ax.legend(fontsize=6.5)
    plt.show()
    return f
    
