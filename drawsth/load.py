# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:22:48 2019

@Author: Zhi-Jiang Yang, Guo-Li Xiong
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; xgl150327@csu.edu.cn
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""


import pandas as pd
import re

def load(file,**kwargs):
    if re.findall('\.xlsx', file) or re.findall('\.xls', file):
        data = pd.read_excel(file,**kwargs)
    elif re.findall('\.csv', file):
        data = pd.read_csv(file,**kwargs)
    elif re.findall('\.txt', file,**kwargs):
        data = pd.read_csv(file,sep='\t')  
    return data



#if '__main__' == __name__:
#    file = 'neg_neg.xlsx'
#    data,label = load(file)