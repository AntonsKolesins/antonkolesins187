# -*- coding: utf-8 -*-
''' Fails : 260.py
Autors: Antons Kolesins
Veidojam tafeli ar uzrakstu: 0123456789ABCDEF
Programma uz tafeles tekstu raksta nesteidzoties:
pa vienam burtam
'''

import Tkinter as tk
import time
root = tk.Tk()
root.title("Mana Tafele ar dinamisku tekstu")

w = tk.Canvas(root, width=600, height=400, \
bg="#456", relief="sunken", border=10 )
w.pack()

t = w.create_text(50, 100, text="2 + 2 = \n4",\
font="Courier 40 bold", fill = "#ffc", anchor="nw")

def funA():
    k = 17
    s = e2.get()
    for i in range(k):
        print s[:i]
        w.itemconfig(t, text=s[:i])
        time.sleep(0.5)
        w.update()

def funB():
    k = 17
    z=b2.get()
    for i in range(k):
        print z[i:]
        w.itemconfig(t, text = z[i:])
        time.sleep(0.5)
        w.update()
    

v = tk.StringVar()
v.set("0123456789ABCDEF")

e2 = tk.Entry(root, textvariable=v)
e2.pack()

b2 = tk.Entry(root, textvariable=v)
b2.pack()

b = tk.Button(root, text="+", command=funA)
b.pack()

b3 = tk.Button(root, text="-", command=funB)
b3.pack()

root.mainloop()

    
