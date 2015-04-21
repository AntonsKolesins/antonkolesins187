# Autors: Antons Kolesins
# -*- coding: utf-8 -*-
#Fails:     250.py
import Tkinter as tk
root = tk.Tk();
root.title("Mana Tafele")
v = tk.StringVar()
v.set('Teksts uz tafeles')
e = tk.Entry(root, textvariable=v)
e.pack()
def fun():
    print e.get()
    w.itemconfig(t, text=e.get())
b = tk.Button(root, text="Spied", command=fun)
b.pack()
w = tk.Canvas(root, width=600, height=400,bg="#456", relief="sunken", border=10 )
w.pack()
t = w.create_text(50, 100, text="2 + 2 = 4", anchor='nw', font="Courier 40 bold italic", fill ="#ffc")
t2 = w.create_text(300, 20, text="Antons Kolesins", anchor='n', font="Courier 40 bold ", fill ="#ffc")
w.mainloop()
