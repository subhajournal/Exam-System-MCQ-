#!/usr/bin/env python
# coding: utf-8

# In[39]:


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pandas as pd
import random
#name=""
qno=[]
exam=pd.read_csv("Exam.csv")


# In[40]:


def qch():
    r=random.randint(0,14)
    if r in qno:
        qch()
    else:
        qno.append(r)
        #print(qno)


# In[41]:


def end(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1200x700')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=1000,y=10)
    lbl=Label(windows,text="Python Examination (Winter Session)",font=("Times New Roman Bold",30)).place(x=150,y=50)
    lbl1=Label(windows,text="Choose any three programs from below: \n",font=("Times New Roman Bold",15)).place(x=150,y=130)
    
    prog='''   1. Write a Python program to remove duplicates from a list.
    2. Write a Python program to check a list is empty or not.
    3. Write a Python program to convert a list of characters into a string
    4. Write a Python program to flatten a shallow list. List1=[[1,2,3],[4,5,6],[7,8,9]]
    5. Write a Python program to check whether a list contains a sublist.
    6. For example: [1,2] is a sublist of mainlist: [3,5,1,2,6,7,8]"
    7. Write a Python program for fetch out the unique elements from a list.
    8. Write a Python program to calculate the ocurrance percentage of charaters in a string.
    9. Write a python program ro arrange a String in ascending order.
    10.Write a Python program to wipe out all the vowels from a String.
    11.Write a Python Program to check the lingest String in a list where the list contaning 12 Strings.
    12.Write a Python program to insert an Addition program into text file.
    13.Take input of 5 students for their NAME, STREAM, ROLL and store all the details into text file.
    14.Write a Python program to count repeated characters in a string.
    15.Write a Python program to print the index of the character in a string.
    16.Write a Python program to find the maximum occurring character in a given string.
    17.Write a Python program to capitalize first and last letters of each word of a given string.
    18.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
    19.Write a Python program that accepts a word from the user and reverse it.'''
    lbl2=Label(windows,text=prog,font=("Times New Roman Bold",12))
    lbl2.place(x=150,y=170)
    lbl2.configure(background="yellow")
    def clicked():
        messagebox.showinfo('Congratulations!!', 'Exam Successfully Finished')
        windows.destroy()
        admin()
    btn=Button(windows,text="End",command=clicked)
    btn.place(x=600,y=600)
    windows.mainloop()


# In[42]:


def e15(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-15",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            end(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[43]:


def e14(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-14",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e15(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[44]:


def e13(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-13",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e14(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[45]:


def e12(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-12",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            #e13(nl[0])
            end(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[46]:


def e11(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-11",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e12(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[47]:


def e10(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-10",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e11(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[48]:


def e9(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-9",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e10(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[49]:


def e8(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-8",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e9(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[50]:


def e7(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-7",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e8(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[51]:


def e6(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-6",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e7(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[52]:


def e5(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-5",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e6(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[53]:


def e4(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-4",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e5(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[54]:


def e3(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-3",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e4(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[55]:


def e2(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-2",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows,text='', value=1, variable=selected)
    rad2 = Radiobutton(windows,text='', value=2, variable=selected)
    rad3 = Radiobutton(windows,text='', value=3, variable=selected)
    rad4 = Radiobutton(windows,text='', value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e3(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()


# In[56]:


def e1(name):
    nl=[name]
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl2=Label(windows,text="Name: "+nl[0],font=("Times New Roman Bold",12)).place(x=750,y=10)
    lbl=Label(windows,text="Question-1",font=("Times New Roman Bold",15)).place(x=150,y=50)
    qch()
    q=Label(windows,text=exam.iloc[qno[-1]][1],font=("Times New Roman Bold",12)).place(x=150,y=90)
    o1=Label(windows,text="1. "+exam.iloc[qno[-1]][2],font=("Times New Roman Bold",12)).place(x=150,y=120)
    o2=Label(windows,text="2. "+exam.iloc[qno[-1]][3],font=("Times New Roman Bold",12)).place(x=150,y=150)
    o3=Label(windows,text="3. "+exam.iloc[qno[-1]][4],font=("Times New Roman Bold",12)).place(x=150,y=180)
    o4=Label(windows,text="4. "+exam.iloc[qno[-1]][5],font=("Times New Roman Bold",12)).place(x=150,y=210)
    selected = IntVar()
    opt=[1,2,3,4]
    rad1 = Radiobutton(windows, value=1, variable=selected)
    rad2 = Radiobutton(windows, value=2, variable=selected)
    rad3 = Radiobutton(windows,value=3, variable=selected)
    rad4 = Radiobutton(windows,value=3, variable=selected)
    rad1.place(x=600,y=120)
    rad2.place(x=600,y=150)
    rad3.place(x=600,y=180)
    rad4.place(x=600,y=210)
    
    def clicked():
        print(selected.get())
        print(type(selected.get()))
        if selected.get() not in opt :
            messagebox.showerror('Answer Error', 'Select an Option')
        else:
            messagebox.showinfo('Sussess', 'Answer Submitted')
            file=open(nl[0]+"-Answers.txt",'a+')
            file.write("Question: "+str(qno[-1])+"    Answer: "+str(selected.get())+"\n")
            file.close()
            windows.destroy()
            e2(nl[0])
    btn=Button(windows,text="Next",command=clicked)
    btn.place(x=480,y=250)
    windows.mainloop()
#e1("n")


# In[77]:


def first():
    windows = Tk()
    windows.title("Python Exam")
    windows.geometry('1000x400')
    lbl=Label(windows,text="Python Examination (Winter Session)",font=("Times New Roman Bold",30)).place(x=150,y=50)
    lbl1=Label(windows,text="Instructions: ",font=("Times New Roman Bold",15)).place(x=150,y=130)
    instr="1. After reading the instructions, Press on Proceed.\n2. In the next page you will enter your first name then press enter\3. After that, you will get the successing questions\n4. You have to answer all the question to get full marks\n5. You have to answer 15 MCQ and have to run 3 programs"
    lbl1=Label(windows,text=instr,font=("Times New Roman Bold",12))
    lbl1.place(x=150,y=170)
    lbl2=Label(windows,text="Enter Name",font=("Times New Roman Bold",15))
    lbl2.place(x=240,y=302)
    lbl1.configure(background="yellow")
    ent=Entry(windows,width=30)
    ent.place(x=350,y=307)
    #nl=[ent.get()]
    def clicked():
        if ent.get()!="":
            #print(ent.get())
            name=ent.get()
            nl=[name]
            
            file=open(nl[0]+"options.txt",'w+')
            file.close()
            windows.destroy()
            e1(nl[0])
            
        else:
            messagebox.showerror('Name Error', 'Name Field cannot be Blank')
    btn=Button(windows,text="Proceed",command=clicked)
    btn.place(x=540,y=305)
    
    windows.mainloop()
first()


# In[ ]:





# In[ ]:




