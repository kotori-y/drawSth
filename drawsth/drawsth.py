# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:30:06 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
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



def warning():
    messagebox.showerror(title='Error!', message="You should choose a Folder!!!")

def choose_loadfile():
    loadfile = askopenfilename(filetypes=(("Excel file", "*.xlsx*;*.xls*"), ("csv file", "*.csv*"), ("Text file", "*.txt*")))
    var_r.set(loadfile)
          
def Draw_roc():
    if var_r.get():
        if var_int.get():
            savefile = asksaveasfilename(filetypes=(("PDF file", "*.pdf*"),("png file", "*.png*")))
        else:
            savefile = None
        draw_roc(var_r.get(), savedir=savefile)
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
        draw_pr(var_r.get(), savedir=savefile)
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
        pic = Enrichment(var_r.get(), savefile=savefile)
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
        logauc(var_r.get(), savedir=savefile)
        if not messagebox.askyesno('Finished!','Would you want to draw others?'):
            root.destroy()
        else:
            pass
    else:
        warning()
    
    
if '__main__' == __name__:
    root = tk.Tk()
    root.geometry('500x300+500+200')
    root.resizable(0,0)
    var_int = tk.IntVar()   
    bbg = tk.Label(root,bg='#fae8eb',width=500,height=300)
    bbg.pack()
    root.title("Let's draw somethings")
        
    btn1 = tk.Button(root, text='Select data file',font=('Arial', 10),command=choose_loadfile,width=15,height=1,bg='#d6c4dd').place(x=35,y=30)
    var_r = tk.StringVar()
    lr = tk.Label(root, textvariable=var_r, bg='#eaf6e8', fg='#494546', font=('Arial', 10),width=38,height=1).place(x=175,y=33)
    
    btn3 = tk.Button(root, text='Draw ROC',font=('Arial', 10),command=Draw_roc,width=15,height=1,bg='#cd1041')
    btn3.place(x=35, y=140)             
                  
    btn4 = tk.Button(root, text='Draw P-R',font=('Arial', 10),command=Draw_pr,width=15,height=1,bg='#cd1041')
    btn4.place(x=35*5, y=140)     

    btn5 = tk.Button(root, text='Draw Enrichment',font=('Arial', 10),command=Draw_enrich,width=15,height=1,bg='#cd1041')
    btn5.place(x=35*9, y=140) 

    btn6 = tk.Button(root, text='Draw logAUC',font=('Arial', 10),command=Draw_logAUC,width=15,height=1,bg='#cd1041')
    btn6.place(x=35*5, y=180) 
    
    c1 = tk.Checkbutton(root, text='Only show', variable=var_int, onvalue=0, offvalue=1, bg='#fae8eb')
    c1.place(x=35*5.5, y=220)
             
    root.mainloop()
    
    
        