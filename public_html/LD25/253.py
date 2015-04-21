# Autors: Antons Kolesins
# -*- coding: utf-8 -*-
#Fails:     253.py

import Tkinter as tk
import tkMessageBox

root = tk.Tk(); root.title("Rezistori")

menubar = tk.Menu(root)
menubar.add_command(label="Aizvērt", command=root.destroy)
root.config(menu=menubar)

w = tk.Canvas(root,width=700, height=200, \
              bg="#996633", relief="sunken", border=10)
w.pack()

krasa=["black","brown","red","orange","yellow","green","blue","purple","gray","white"]
tkrasa = ["white","black","black","black","black","black","black","black","black","black",]

x=150
y=45
t1=w.create_text(100,30,text="Rezistori", font="Courier 14")
for i in range(len(krasa)):
 w.create_rectangle(x,y,x+40,y+20, fill=krasa[i])
 num = w.create_text(x+15, y+10, anchor='w',text=i, font="Courier 15", fill = tkrasa[i])
 x=x+41

x=150
y=75
for i in range(len(krasa)):
 w.create_rectangle(x,y,x+40,y+20, fill=krasa[i])
 num = w.create_text(x+15, y+10, anchor='w',text=i, font="Courier 15", fill = tkrasa[i])
 x=x+41

x=150
y=100
for i in range(len(krasa)):
 w.create_rectangle(x,y,x+40,y+20, fill=krasa[i])
 num = w.create_text(x+15, y+10, anchor='w',text=i, font="Courier 15", fill = tkrasa[i])
 x=x+41

reizkrasa=["#C0C0C0","#FFD700","black","brown","red","orange","yellow","green","blue","purple"]
reiztkrasa = ["black","black","white","black","black","black","black","black","black","black"]
reizinatajs = ["0.01","0.1","1","10","100","1k","10k","100k","1M","10M"]

x=67.5
y=125
t1=w.create_text(545,135,text="Reizinatajs", font="Courier 12")
for i in range(len(reizkrasa)):
 w.create_rectangle(x,y,x+40,y+20, fill=reizkrasa[i])
 num = w.create_text(x+6, y+10, anchor='w',text=reizinatajs[i], font="Courier 11", fill = reiztkrasa[i])
 x=x+41

tolkrasa = ["#C0C0C0","#FFD700","white","brown","red"]
tolerance= ["10%","5%","0","1%","2%"]

x=67.5
y=150
t1=w.create_text(545,165,text="Tolerance", font="Courier 12")
for i in range(len(tolkrasa)):
 w.create_rectangle(x,y,x+40,y+20, fill=tolkrasa[i])
 num = w.create_text(x+7, y+10, anchor='w',text=tolerance[i], font="Courier 11", fill = "black")
 x=x+41


w.mainloop()
