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
import numpy as np
import warnings

warnings.filterwarnings("ignore")

LAM = 0.001
STEP = 0.001


def logauc(file, label_col, ascore_col, dscore_col, figsize=(5, 5)):
    # 此处传两个参数，file为格式为xlsx的数据文件；savedir为图片保存的路径
    data = load(file)
    score_col = [*ascore_col, *dscore_col]

    pos_num = data[label_col].values.sum()
    neg_num = len(data) - pos_num
    # times = neg//pos

    decoy_found = np.log10(np.arange(LAM, 1 + STEP, STEP)) + 2

    fig, ax = plt.subplots(figsize=figsize)

    for col in score_col:
        resl = []
        v = data.loc[:, [label_col, col]].copy()
        # df.drop(['mol','number','name'],axis=1,inplace=True)

        ascending = col in ascore_col
        v.sort_values(col, ascending=ascending, inplace=True)
        v = v.reset_index(drop=True)

        neg_idx = v[v[label_col] == 0].index.tolist()

        ligandf = []

        for ratio in np.arange(LAM, 1 + STEP, STEP):
            n_decoy_found = max(math.floor(neg_num * ratio) - 1, 0)
            df_i = v.iloc[:neg_idx[n_decoy_found], :]
            n_ligand_found = df_i[label_col].sum()

            ligandf.append(round(n_ligand_found / pos_num, 2) * 100)

        for index in np.arange(len(decoy_found) - 1):
            x_i = (10 ** decoy_found[index]) / 100
            x_i_ = (10 ** decoy_found[index + 1]) / 100

            y_i = ligandf[index] / 100
            y_i_ = ligandf[index + 1] / 100

            bi = y_i_ - x_i_ * ((y_i_ - y_i) / (x_i_ - x_i))

            res = ((y_i_ - y_i) / log(10, math.e)) + bi * (log10(x_i_) - log10(x_i))
            resl.append(res)

        logAuc = sum(resl) / log10(1 / LAM)
        plt.plot(decoy_found, ligandf, label=''.join([col, ' logAUC=%.3f' % logAuc]))

    resl = []

    ligandrandl = [10 ** i for i in decoy_found]

    for index in range(len(decoy_found) - 1):
        rx_i = (10 ** decoy_found[index]) / 100
        rx_i_ = (10 ** decoy_found[index + 1]) / 100

        ry_i = ligandrandl[index] / 100
        ry_i_ = ligandrandl[index + 1] / 100

        bi = ry_i_ - rx_i_ * ((ry_i_ - ry_i) / (rx_i_ - rx_i))

        res = ((ry_i_ - ry_i) / log(10, math.e)) + bi * (log10(rx_i_) - log10(rx_i))
        resl.append(res)
    rlogAuc = sum(resl) / log10(1 / LAM)

    plt.plot(decoy_found, ligandrandl, linestyle='--', label=''.join(['Random', ' logAUC=%.3f' % rlogAuc]), color='black')
    ax.tick_params(width=1.3)
    ax.set_xticks([-1, 0, 1, 2])
    ax.set_xticklabels(['$\mathregular{10^{-1}}$',
                        '$\mathregular{10^{0}}$',
                        '$\mathregular{10^{1}}$',
                        '$\mathregular{10^{2}}$'])
    ax.set_xlim([-1, 2])
    ax.set_ylim([0, 100])
    ax.spines['bottom'].set_linewidth(1.3)
    ax.spines['left'].set_linewidth(1.3)
    ax.spines['top'].set_linewidth(1.3)
    ax.spines['right'].set_linewidth(1.3)
    ax.set_xlabel('% Decoys Found', size=13)
    ax.set_ylabel('% Ligands Found', size=13)
    ax.tick_params(direction='in', which='both', labelsize=12)
    ax.legend(fontsize=7)
    plt.show()
    return fig
