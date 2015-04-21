
#Autors: Antons Kolesins
# -*- coding: utf-8 -*-
from Tkinter import *
w = Tk ()
w.title ('Antons Kolesins ')
uzr01 = Label(w,fg='blue', text='Datormācības(speckurss),')
uzr02 = Label(w,fg='blue', text="ETP,")
uzr03 = Label(w, fg='blue',text='Fizika,')
uzr04 = Label(w,fg='blue', text='Datormācību LD')
uzr05 = Label(w,font ='family(Time,Helvetica,Symbol,Courier)', text="Antons Kolesins ")
uzr06 = Label(w, text='141REB187')
uzr07 = Label(w, text='RTU, ETF, 2015')
uzr01.place(x=0, y = 20 )
uzr02.place(x=0, y = 40 )
uzr03.place(x=0, y = 60 )
uzr04.place(x=0, y = 80 )
uzr05.place(x=40, y = 100 )
uzr06.place(x=40, y = 120 )
uzr07.place(x=40, y = 140 )
w.geometry('300x200')
w.mainloop()


