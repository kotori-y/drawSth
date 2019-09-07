# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:25:35 2019

@Author: Zhi-Jiang Yang, Guo-Li Xiong
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; xgl150327@csu.edu.cn
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""


import math
import matplotlib.pyplot as plt
from math import log
from math import log10
from load import load
import warnings
warnings.filterwarnings("ignore")


def logauc(file, label_col, score_col, savedir=None, figsize=(5,5)):
    #此处传两个参数，file为格式为xlsx的数据文件；savedir为图片保存的路径
    data = load(file)
    df = data
    pos = len(df[df[label_col]==1])
    neg = len(df[df[label_col]==0])
    times = neg//pos
    ligandrandl = list()

    f,ax = plt.subplots(figsize=figsize)

    for col in score_col:
        resl = list()
        v = df.copy()
        v = v.loc[:,[label_col,col]]
        #df.drop(['mol','number','name'],axis=1,inplace=True)
        if (df[col]<0).all():
            ascending = 1
        else:
            ascending = 0
        v.sort_values(col,ascending=ascending,inplace=True)

        counter = 0
        index = -1
        Lam = 0.001

        percent = Lam

        ligandf = list()
        decoyf = list()

        for item in list(v[label_col]):
            index += 1
            if item == 0:
                counter += 1
                if counter == int(neg*percent):

                    df_i = v.iloc[:index+1,:]

                    dic = df_i[label_col].value_counts()

                    try:
                        linum = dic[1]
                    except KeyError:
                        linum = 0

                    ligandf.append(round(linum/pos,2)*100)
                    decoyf.append(math.log10(percent)+2)
                    if col == score_col[0]:
                        ligandrand = counter//times
                        ligandrandl.append(round(ligandrand/pos,2)*100)

                    percent += 0.001
                    
        e = math.e
        
        for index in range(999):
            x_i = (10**decoyf[index])/100
            x_i_ = (10**decoyf[index+1])/100

            y_i = ligandf[index]/100
            y_i_ = ligandf[index+1]/100

            bi = y_i_ - x_i_*((y_i_-y_i)/(x_i_-x_i))


            res = ((y_i_-y_i)/log(10,e))+bi*(log10(x_i_)-log10(x_i))
            resl.append(res)
            

        logAuc = sum(resl)/log10(1/Lam)
        plt.plot(decoyf,ligandf,label=''.join([col,' logAUC=%.3f' %logAuc]))
    
    resl = []
    for index in range(999):
        rx_i = (10**decoyf[index])/100
        rx_i_ = (10**decoyf[index+1])/100

        ry_i = ligandrandl[index]/100
        ry_i_ = ligandrandl[index+1]/100

        bi = ry_i_ - rx_i_*((ry_i_-ry_i)/(rx_i_-rx_i))


        res = ((ry_i_-ry_i)/log(10,e))+bi*(log10(rx_i_)-log10(rx_i))
        resl.append(res)
    rlogAuc = sum(resl)/log10(1/Lam)
        
        
        
    plt.plot(decoyf,ligandrandl,linestyle='--',label=''.join(['Random',' logAUC=%.3f' %rlogAuc]),color='black')
    ax.tick_params(width=1.3)
    ax.set_xticks([-1,0,1,2])
    ax.set_xticklabels(['10^-1','10^0','10^1','10^2'])
    ax.set_xlim([-1,2])
    ax.set_ylim([0,100])
    ax.spines['bottom'].set_linewidth(1.3)
    ax.spines['left'].set_linewidth(1.3)
    ax.spines['top'].set_linewidth(1.3)
    ax.spines['right'].set_linewidth(1.3) 
    ax.set_xlabel('% Decoys Found',size=13)
    ax.set_ylabel('% Ligands Found',size=13)
    ax.tick_params(direction='in', which='both', labelsize=12)
    ax.legend(fontsize=7)
    if savedir:
        plt.savefig(savedir)
    else:
        pass
    plt.show()
    
    
if '__main__' == __name__:       
    logauc('pos_neg.xlsx', label_col='Label',score_col=['ASP','PLP'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
