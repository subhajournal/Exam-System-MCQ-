from tkinter import *
from tkinter import messagebox
import os

def admin():
    windows = Tk()
    windows.title("Exam Login")
    windows.geometry('270x200')
    windows.configure(background="cyan")
    lbl=Label(windows,text="Admin ID",font=("Times New Roman Bold",12))
    lbl.place(x=30,y=50)
    lbl.configure(background="cyan")
    uid=Entry(windows,width=20)
    uid.place(x=100,y=50)
    lb2=Label(windows,text="Password",font=("Times New Roman Bold",12))
    lb2.place(x=30,y=80)
    lb2.configure(background="cyan")
    pss=Entry(windows,width=20, show="*")
    pss.place(x=100,y=80)
    def clicked():
        if uid.get()=="admin" and pss.get()=="1234!!":
            windows.destroy()
            os.system("Exam_Python.py")
        else:
            messagebox.showerror('Error Message', 'Error in Credential!!')
    btn=Button(windows,text="Start",command=clicked)
    btn.place(x=100,y=120)
    windows.mainloop()
admin()
