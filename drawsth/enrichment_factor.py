# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:37:57 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from load import load
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


class EF(object):
    """
    """
    def __init__(self, loadfile, label_col, Ascore_col, Dscore_col, pic_savefile=None, df_savefile=None):
        self.loadfile = loadfile
        self.pic_savefile = pic_savefile
        self.df_savefile = df_savefile
        self.length = 0
        self.hit_all = 0
        self.scores = pd.Series()
        self.score_col = Ascore_col + Dscore_col
        self.Ascore = Ascore_col
        self.Dscore = Dscore_col
        self.label_col = label_col
            
    def Load(self):
        self.df = load(self.loadfile)
        self.all_mol = len(self.df)
        self.all_active = len(self.df[self.df[self.label_col]==1])
#        self.scorers = pd.Series(self.score_col)
        
    def calculateEF(self):
        """
        """        
        thres = [0.001, 0.005, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.50]
        df_o = pd.DataFrame(index=thres)

        for simi in self.score_col:
            self.df.sort_values(simi, ascending=0, inplace=True)
            label_sort = self.df[self.label_col]
            efl = []
            
            for thre in thres:
                part_mol = label_sort[:math.floor(self.all_mol*thre)]
                part_active = part_mol.sum()             
                ef = (part_active/len(part_mol))/(self.all_active/self.all_mol)
                efl.append(ef)
            df_o[simi] = efl
        df_o['average'] = df_o.apply(lambda x: x.mean(),axis=1)
        df_o.to_csv(self.df_savefile,index_label='Similarity')
     
    def drawEF(self):
        """
        """
        f,ax = plt.subplots()
        axins = inset_axes(ax, width="40%", height="40%")
        font_kws = {'family':'arial','size':18}
        efl = []
        
        
        for simi in self.score_col:
            self.df.sort_values(simi, ascending=0, inplace=True)
            label_sort = self.df[self.label_col]
        
            for thre in np.arange(0.001,1.001,0.001):
                part_mol = label_sort[:math.floor(self.all_mol*thre)]
                part_active = part_mol.sum()
            
                ef = (part_active/len(part_mol))/(self.all_active/self.all_mol)
                efl.append(ef)
    #              
        efl = np.array(efl).reshape(len(self.score_col), len(np.arange(0.001,1.001,0.001))).T
        efl = [item.mean() for item in efl]
        ax.plot(np.arange(0.001,1.001,0.001), efl)
        axins.plot(np.arange(0.001,0.201,0.001), efl[:200])
        ax.set_xlabel('Fraction of Samples', fontdict=font_kws)
        ax.set_ylabel('Enrichment Factor', fontdict=font_kws)
        ax.tick_params(direction='in', which='both', labelsize=12)
        axins.tick_params(direction='in', which='both', labelsize=8, length=2)
           
        if self.pic_savefile:
            plt.savefig(self.pic_savefile)
        else:
            pass
        plt.show()
            
            
            
if '__main__' == __name__:
    ef = EF(loadfile=r'C:\Users\0720\Desktop\MATE\akuma\ef_demo.csv',
            label_col='Label',
            Dscore_col=[
                    'similarity','similarity (Iter #1)', 'similarity (Iter #2)',
                    'similarity (Iter #3)','similarity (Iter #4)', 'similarity (Iter #5)',
                    'similarity (Iter #6)','similarity (Iter #7)', 'similarity (Iter #8)',
                    'similarity (Iter #9)','similarity (Iter #10)', 'similarity (Iter #11)',
                    'similarity (Iter #12)', 'similarity (Iter #13)','similarity (Iter #14)',
                    'similarity (Iter #15)','similarity (Iter #16)'],pic_savefile=r'C:\Users\0720\Desktop\MATE\akuma\ef_demo.pdf',Ascore_col=[],df_savefile=r'C:\Users\0720\Desktop\MATE\akuma\demo.csv')
    ef.Load()
    ef.drawEF()
    ef.calculateEF()
            
            
            
            
            
            
            
            
            
            
            