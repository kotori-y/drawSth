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

def Help():
    messagebox.showinfo(title='Help',message='There are three listboxes:\
                        \nlabel: the target name;\
                        \nAscending Scores: target scores, more lower more likely to be positive class;\
                        \nDscending Scores: target scores, more higher more likely to be positive class.\
                        \nTarget scores, can either be probability estimates of the positive class,confidence values, or non-thresholded measure of decisions.\
                        \n\nThe "only show" checkbox meant would not save the output')
  
def About():
    messagebox.showinfo(title='About',message='Version:1.1\
                        \n@Author: Zhi-Jiang Yang, Guo-Li Xiong\
                        \n@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China\
                        \n@Homepage: http://www.scbdd.com\
                        \n@Mail: yzjkid9@gmail.com; xgl150327@csu.edu.cn\
                        \nBlog: https://blog.moyule.me')

    
def choose_loadfile():
    loadfile = askopenfilename(filetypes=(("Excel file", "*.xlsx*;*.xls*"), ("csv file", "*.csv*"), ("Text file", "*.txt*")))
    var_r.set(loadfile)    
    lb.delete(0,tk.END)
    lb_label.delete(0,tk.END)
    lb_Ascore.delete(0,tk.END)
    lb_Dscore.delete(0,tk.END)
    if var_r.get():
        cols = list(load(loadfile).columns)      
        var_scores.set(cols)

  
def Draw_roc():
    if var_r.get():
        if var_int.get():
            savefile = asksaveasfilename(filetypes=(("PDF file", "*.pdf*"),("png file", "*.png*")))
        else:
            savefile = None
        label = lb_label.get(0,tk.END)[0]
        Ascores = lb_Ascore.get(0,tk.END)
        Dscores = lb_Dscore.get(0,tk.END)
        draw_roc(var_r.get(), label_col=label, Ascore_col=Ascores, Dscore_col=Dscores, savedir=savefile)
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
        Ascores = lb_Ascore.get(0,tk.END)
        Dscores = lb_Dscore.get(0,tk.END)
        draw_pr(var_r.get(), label_col=label, Ascore_col=Ascores, Dscore_col=Dscores, savedir=savefile)
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
        Ascores = lb_Ascore.get(0,tk.END)
        Dscores = lb_Dscore.get(0,tk.END)
        pic = Enrichment(var_r.get(), label_col=label, Ascore_col=Ascores, Dscore_col=Dscores, savefile=savefile)
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
        Ascores = lb_Ascore.get(0,tk.END)
        Dscores = lb_Dscore.get(0,tk.END)
        logauc(var_r.get(), label_col=label, Ascore_col=Ascores, Dscore_col=Dscores, savedir=savefile)
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

def lbtoAscore():
    indexs = lb.curselection()[::-1]
    for idx in indexs: 
        lb_Ascore.insert('end',lb.get(idx))
        lb.delete(idx)

def lbtoDscore():
    indexs = lb.curselection()[::-1]
    for idx in indexs: 
        lb_Dscore.insert('end',lb.get(idx))
        lb.delete(idx)

def labeltolb():
    indexs = lb_label.curselection()[::-1]
    for idx in indexs: 
        lb.insert('end',lb_label.get(idx))
        lb_label.delete(idx)

def Ascoretolb():
    indexs = lb_Ascore.curselection()[::-1]
    for idx in indexs: 
        lb.insert('end',lb_Ascore.get(idx))
        lb_Ascore.delete(idx)

def Dscoretolb():
    indexs = lb_Dscore.curselection()[::-1]
    for idx in indexs: 
        lb.insert('end',lb_Dscore.get(idx))
        lb_Dscore.delete(idx)

 
if '__main__' == __name__:
    root = tk.Tk()
    root.geometry('600x370+500+200')
    root.resizable(0,0)
    var_int = tk.IntVar()   
    bbg = tk.Label(root,bg='#fae8eb',width=500,height=300)
    bbg.pack()
    root.title("Let's draw somethings")
    
    
    menubar = tk.Menu(root)
    menubar.add_command(label = "Help", command=Help)
    menubar.add_command(label = "About", command=About)
    
    
    var_label = tk.StringVar()
    var_scores = tk.StringVar()
    
    
    btn1 = tk.Button(root, text='Select data file',font=('Arial', 10),command=choose_loadfile,width=15,height=1,bg='#d6c4dd').place(x=35,y=20)
    var_r = tk.StringVar()
    lr = tk.Label(root, textvariable=var_r, bg='#eaf6e8', fg='#494546', font=('Arial', 10),width=45,height=1).place(x=175,y=23)
    
    btn3 = tk.Button(root, text='Draw ROC',font=('Arial', 10),command=Draw_roc,width=15,height=1,bg='#cd1041')
    btn3.place(x=430, y=95)             
                  
    btn4 = tk.Button(root, text='Draw P-R',font=('Arial', 10),command=Draw_pr,width=15,height=1,bg='#cd1041')
    btn4.place(x=430, y=135)     

    btn5 = tk.Button(root, text='Draw Enrichment',font=('Arial', 10),command=Draw_enrich,width=15,height=1,bg='#cd1041')
    btn5.place(x=430, y=175) 

    btn6 = tk.Button(root, text='Draw logAUC',font=('Arial', 10),command=Draw_logAUC,width=15,height=1,bg='#cd1041')
    btn6.place(x=430, y=215) 
    
    c1 = tk.Checkbutton(root, text='Only show', variable=var_int, onvalue=0, offvalue=1, bg='#fae8eb')
    c1.place(x=450, y=220+30)
     
    lb = tk.Listbox(root,selectmode='extended',listvariable=var_scores)
    lb.place(x=35,y=60,relwidth=0.3,relheight=0.8)
    scrollbar = tk.Scrollbar(lb,command=lb.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Label',bg='#fae8eb').place(x=35*9, y=50+5)
    lb_label = tk.Listbox(root,selectmode='extended')
    lb_label.place(x=35*8, y=70+5, relwidth=0.2, relheight=0.2)
    scrollbar = tk.Scrollbar(lb_label,command=lb_label.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_label.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Ascending Scores',bg='#fae8eb').place(x=35*8+5, y=145+5)
    lb_Ascore = tk.Listbox(root,selectmode='extended')
    lb_Ascore.place(x=35*8, y=165+5, relwidth=0.2, relheight=0.2)
    scrollbar = tk.Scrollbar(lb_Ascore,command=lb_Ascore.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_Ascore.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Descending Scores',bg='#fae8eb').place(x=35*8+5, y=235+5)
    lb_Dscore = tk.Listbox(root,selectmode='extended')
    lb_Dscore.place(x=35*8, y=255+5, relwidth=0.2, relheight=0.2)
    scrollbar = tk.Scrollbar(lb_Dscore,command=lb_Dscore.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_Dscore.config(yscrollcommand=scrollbar.set)
    
    
    
    theButton = tk.Button(root, text="→", command=lbtolabel, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=70+5)
    theButton = tk.Button(root, text="←", command=labeltolb, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=110+5)
    
    theButton = tk.Button(root, text="→", command=lbtoAscore, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=168+5)
    theButton = tk.Button(root, text="←", command=Ascoretolb, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=208+5)                   
    
    theButton = tk.Button(root, text="→", command=lbtoDscore, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=258+5)
    theButton = tk.Button(root, text="←", command=Dscoretolb, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=298+5)
        
    root.iconbitmap('ico.ico')  
    root.config(menu = menubar)
    root.mainloop()
    
    
        