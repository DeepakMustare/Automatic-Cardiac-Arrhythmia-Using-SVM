# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Classification of Cardiac Arrhythmia Using SVM")
 
image2 = Image.open('bg1.jpg')
image2 = image2.resize((1400, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=200, y=0)       

def reg():
    from subprocess import call
    call(["python","new registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()
        
Login_frame=tk.Frame(root,bg="#ffd666",height=900,width=300)
Login_frame.place(x=0,y=0)

l2 = tk.Label(Login_frame, text="HOME", width=12, font=("Times new roman", 25, "bold"), bg="#ffd666")
l2.place(x=25, y=30)

button1 = tk.Button(Login_frame, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="white", fg="black")
button1.place(x=25, y=200)

button2 = tk.Button(Login_frame, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="white", fg="black")
button2.place(x=25, y=300)

button3 = tk.Button(Login_frame, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="white", fg="black")
button3.place(x=25, y=400)
root.mainloop()