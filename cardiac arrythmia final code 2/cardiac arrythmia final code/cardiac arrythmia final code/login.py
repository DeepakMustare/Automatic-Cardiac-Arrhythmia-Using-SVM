import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2

##############################################+=============================================================
root = tk.Tk()
root.configure(background="gray")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

image2 = Image.open('4.png')
image2 = image2.resize((900, 800), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

username = tk.StringVar()
password = tk.StringVar()
        
def master():
    from subprocess import call
    call(["python","emp GUI_Master.py"])
    root.destroy()
def registration():
    from subprocess import call
    call(["python","new registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()
         print(result)
         for row in result:
             print("id=",row[0],)
             id=str(row[0])
             print(id)
             with open(r"F:\cardiac arrythmia final code 2\cardiac arrythmia final code\cardiac arrythmia final code\id.txt", 'w') as f:
                 
             
                f.write(str(id))
             # f1=open("id.txt","w")
             # f1.write(str(id))
         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
           
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            from subprocess import call
            call(["python","emp GUI_Master.py"])
            root.destroy()
            root.destroy()
            
            # ===========================================
          

            

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


        
Login_frame=tk.Frame(root,bg="#c1c1c1",width=575,height=400)
Login_frame.place(x=930,y=200)

title=tk.Label(Login_frame, text="Login Here", font=("CALIBRI", 30, "bold"),bd=5,bg="#c1c1c1",fg="black")
title.place(x=175,y=40,width=250)
       
lbluser=tk.Label(Login_frame,text="Username",compound=LEFT,font=("CALIBRI", 20,"bold"),bg="#c1c1c1",fg="black").place(x=30,y=120,width=250)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.place(x=280,y=130,width=250)
       
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("CALIBRI", 20, "bold"),bg="#c1c1c1",fg="black").place(x=30,y=180,width=250)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.place(x=280,y=180,width=250)
       
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("calibri", 16, "bold"),bg="#E70045",fg="black")
btn_log.place(x=52,y=260,width=475)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("calibri", 14, "bold"),bg="#EBECF0",fg="black")
btn_reg.place(x=170,y=330,width=250)
        
        
    

root.mainloop()