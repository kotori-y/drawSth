# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:22:48 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""


import pandas as pd
import re

def load(file, labelcol='Label', unexpec_col = []):
    if re.findall('\.xlsx', file) or re.findall('\.xls', file):
        data = pd.read_excel(file)
    elif re.findall('\.csv', file):
        data = pd.read_csv(file)
    elif re.findall('\.txt', file):
        data = pd.read_txt(file,sep='\t')
    
    label = data.pop('Label')
    data.drop(unexpec_col,axis=1,inplace=True)
    return data,label



#if '__main__' == __name__:
#    file = 'neg_neg.xlsx'
#    data,label = load(file)