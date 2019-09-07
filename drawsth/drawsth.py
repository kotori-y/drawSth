# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:30:06 2019

@Author: Zhi-Jiang Yang, Guo-Li Xiong
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; xgl150327@csu.edu.cn
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from draw_roc import draw_roc
from draw_pr import draw_pr
from draw_enrichment import Enrichment 
from draw_logauc import logauc
from load import load


def warning():
    messagebox.showerror(title='Error!', message="You should choose a Folder!!!")

def choose_loadfile():
    loadfile = askopenfilename(filetypes=(("Excel file", "*.xlsx*;*.xls*"), ("csv file", "*.csv*"), ("Text file", "*.txt*")))
    var_r.set(loadfile)
    cols = list(load(loadfile).columns)   
    for col in cols:
        lb.insert("end", col)
   
def Draw_roc():
    if var_r.get():
        if var_int.get():
            savefile = asksaveasfilename(filetypes=(("PDF file", "*.pdf*"),("png file", "*.png*")))
        else:
            savefile = None
        label = lb_label.get(0,tk.END)[0]
        scores = lb_score.get(0,tk.END)
        draw_roc(var_r.get(), label_col=label, score_col=scores, savedir=savefile)
        if not messagebox.askyesno('Finished!','Would you want to draw others?'):
            root.destroy()
        else:
            pass
    else:
        warning()
            
def Draw_pr():
    if var_r.get():
        if var_int.get():
            savefile = asksaveasfilename(filetypes=(("PDF file", "*.pdf*"),("png file", "*.png*")))
        else:
            savefile = None
        label = lb_label.get(0,tk.END)[0]
        scores = lb_score.get(0,tk.END)
        draw_pr(var_r.get(), label_col=label, score_col=scores, savedir=savefile)
        if not messagebox.askyesno('Finished!','Would you want to draw others?'):
            root.destroy()
        else:
            pass 
    else:
        warning()
    
def Draw_enrich():
    if var_r.get():
        if var_int.get():
            savefile = asksaveasfilename(filetypes=(("PDF file", "*.pdf*"),("png file", "*.png*")))
        else:
            savefile = None
        label = lb_label.get(0,tk.END)[0]
        scores = lb_score.get(0,tk.END)
        pic = Enrichment(var_r.get(), label_col=label, score_col=scores, savefile=savefile)
        pic.show_enrichment_roc()
        if not messagebox.askyesno('Finished!','Would you want to draw others?'):
            root.destroy()
        else:
            pass
    else:
        warning()

def Draw_logAUC():
    if var_r.get():
        if var_int.get():
            savefile = asksaveasfilename(filetypes=(("PDF file", "*.pdf*"),("png file", "*.png*")))
        else:
            savefile = None
        label = lb_label.get(0,tk.END)[0]
        scores = lb_score.get(0,tk.END)
        logauc(var_r.get(), label_col=label, score_col=scores, savedir=savefile)
        if not messagebox.askyesno('Finished!','Would you want to draw others?'):
            root.destroy()
        else:
            pass
    else:
        warning()
   
def lbtolabel(): 
    indexs = lb.curselection()[::-1]
    for idx in indexs: 
        lb_label.insert('end',lb.get(idx))
        lb.delete(idx)

def lbtoscore():
    indexs = lb.curselection()[::-1]
    for idx in indexs: 
        lb_score.insert('end',lb.get(idx))
        lb.delete(idx)

def labeltolb():
    indexs = lb_label.curselection()[::-1]
    for idx in indexs: 
        lb.insert('end',lb_label.get(idx))
        lb_label.delete(idx)

def scoretolb():
    indexs = lb_score.curselection()[::-1]
    for idx in indexs: 
        lb.insert('end',lb_score.get(idx))
        lb_score.delete(idx)
 
if '__main__' == __name__:
    root = tk.Tk()
    root.geometry('500x300+500+200')
    root.resizable(0,0)
    var_int = tk.IntVar()   
    bbg = tk.Label(root,bg='#fae8eb',width=500,height=300)
    bbg.pack()
    root.title("Let's draw somethings")
         
    btn1 = tk.Button(root, text='Select data file',font=('Arial', 10),command=choose_loadfile,width=15,height=1,bg='#d6c4dd').place(x=35,y=20)
    var_r = tk.StringVar()
    lr = tk.Label(root, textvariable=var_r, bg='#eaf6e8', fg='#494546', font=('Arial', 10),width=38,height=1).place(x=175,y=23)
    
    btn3 = tk.Button(root, text='Draw ROC',font=('Arial', 10),command=Draw_roc,width=15,height=1,bg='#cd1041')
    btn3.place(x=35, y=140+40)             
                  
    btn4 = tk.Button(root, text='Draw P-R',font=('Arial', 10),command=Draw_pr,width=15,height=1,bg='#cd1041')
    btn4.place(x=35*5, y=140+40)     

    btn5 = tk.Button(root, text='Draw Enrichment',font=('Arial', 10),command=Draw_enrich,width=15,height=1,bg='#cd1041')
    btn5.place(x=35*9, y=140+40) 

    btn6 = tk.Button(root, text='Draw logAUC',font=('Arial', 10),command=Draw_logAUC,width=15,height=1,bg='#cd1041')
    btn6.place(x=35*5, y=180+40) 
    
    c1 = tk.Checkbutton(root, text='Only show', variable=var_int, onvalue=0, offvalue=1, bg='#fae8eb')
    c1.place(x=35*5.5, y=220+40)
     
    lb = tk.Listbox(root,selectmode='extended')
    lb.place(x=175,y=50,relwidth=0.3,relheight=0.4)
    scrollbar = tk.Scrollbar(lb,command=lb.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Label',bg='#fae8eb').place(x=60, y=50)
    lb_label = tk.Listbox(root,selectmode='extended')
    lb_label.place(x=30, y=70, relwidth=0.2, relheight=0.3)
    scrollbar = tk.Scrollbar(lb_label,command=lb_label.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_label.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Scores',bg='#fae8eb').place(x=60*6+35, y=50)
    lb_score = tk.Listbox(root,selectmode='extended')
    lb_score.place(x=30*12+10, y=70, relwidth=0.2, relheight=0.3)
    scrollbar = tk.Scrollbar(lb_score,command=lb_score.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_score.config(yscrollcommand=scrollbar.set)
    
    
    theButton = tk.Button(root, text="←", command=lbtolabel, bg='#cd1041', width=3, height=1)
    theButton.place(x=140,y=80)
    theButton = tk.Button(root, text="→", command=labeltolb, bg='#cd1041', width=3, height=1)
    theButton.place(x=140,y=120)
    
    theButton = tk.Button(root, text="→", command=lbtoscore, bg='#cd1041', width=3, height=1)
    theButton.place(x=330,y=80)
    theButton = tk.Button(root, text="←", command=scoretolb, bg='#cd1041', width=3, height=1)
    theButton.place(x=330,y=120)                   
    
    label = lb_label.get(0,tk.END)
    scores = lb_score.get(0,tk.END)
    
    root.iconbitmap('ico.ico')
    root.mainloop()
    
    
        