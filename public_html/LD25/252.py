# Autors: Antons Kolesins
# -*- coding: utf-8 -*-
#Fails:     252.py
import Tkinter as tk
root= tk.Tk()
root.title("Mana Bilde")
w = tk.Canvas(root, width=800, height=800, bg="#abc")
w.pack()
linija = w.create_line(50, 450, 50, 0, fill="#ffffff", width="16")
linija2 = w.create_line(150, 450, 150, 0, fill="#ffff00", width="16")
linija3 = w.create_line(250, 450, 250, 0, fill="#00ffff", width="16")
linija4 = w.create_line(350, 450, 350, 0, fill="#00ff00", width="16")
linija5 = w.create_line(450, 450, 450, 0, fill="#551a8b", width="16")
linija6 = w.create_line(550, 450, 550, 0, fill="#ff0000", width="16")
linija7 = w.create_line(650, 450, 650, 0, fill="#0000ff", width="16")
linija8 = w.create_line(750, 450, 750, 0, fill="#000000", width="16")
t2=w.create_text(376, 400, text="Patricija Dumina krasu tabula", font="Hlvetica 20 normal")
root.mainloop()
