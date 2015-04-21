# Autors: Antons Kolesins
# -*- coding: utf-8 -*-
#Fails:     251.py
import Tkinter as tk

root= tk.Tk()
root.title("Mana Bilde")
w = tk.Canvas(root, width=600, height=400, bg="#abc")
w.pack()
linija = w.create_line(50, 100, 400, 300)

root.mainloop()
