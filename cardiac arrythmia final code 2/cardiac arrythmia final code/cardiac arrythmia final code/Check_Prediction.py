from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    import sklearn
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    import sqlite3

    from PIL import Image, ImageTk
    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title(" Classification of Cardiac Arrhythmia using SVM")
    root.configure(background="LightSkyBlue")
    
    

# Create a photoimage object of the image in the path
    image1 = Image.open("F:/cardiac arrythmia final code 2/cardiac arrythmia final code/cardiac arrythmia final code/10.jpg")
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test

# Position image
    label1.place(x=800, y=10)

    
    record= tk.IntVar()
    preRR= tk.IntVar()
    postRR = tk.IntVar()
    pPeak = tk.IntVar()
    tPeak= tk.IntVar()
    rPeak = tk.IntVar()
    sPeak =  tk.IntVar()
    qPeak = tk.IntVar()
    qrs_interval = tk.IntVar()


    
    
    #===================================================================================================================



    def Detect():
        root = tk.Tk()

        root.geometry("800x850+250+5")
        root.title(" Classification of Cardiac Arrhythmia using SVM")
        root.configure(background="white")
       
        
        
        
        e1=record.get()
        print(e1)
        e2=preRR.get()
        print(e2)
        e3=postRR.get()
        print(e3)
        e4=pPeak.get()
        print(e4)
        e5=tPeak.get()
        print(e5)
        e6=rPeak.get()
        print(e6)
        e7=sPeak.get()
        print(e7)
        e8=qPeak .get()
        print(e8)
        e9=qrs_interval.get()
        print(e9)
        
        sqliteConnection = sqlite3.connect('evaluation1.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
       
        f1=open("id.txt","r")
        id=f1.read()
        print("ID", id)
        f1.close()
    
        
        #########################################################################################
        
       
        from joblib import dump , load
        a1=load('F:/cardiac arrythmia final code 2/cardiac arrythmia final code\cardiac arrythmia final code/card_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9]])
        print(v)
    
        if v[0]=='VEB':
           print("VEB(Ventricular ectopic beat)")
           yes = tk.Label(root,wraplength=1565,text=" Your Result :\n VEB(Ventricular ectopic beat) \n___Remedies___\n * \nThe best ways to prevent tachycardia are to maintain\n a healthy heart and prevent heart disease.\nIf you already have heart disease, monitor it and follow your treatment plan.\n Be sure you understand your treatment plan, and take all medications as prescribed. \n\nTake the following steps to keep the heart healthy:\nEat a balanced, nutritious diet:\n A diet low in saturated and trans fats and rich in fruits, vegetables and whole grains helps keep the heart healthy.\n Exercise and maintain a healthy weight: \nBeing overweight increases the risk of developing heart disease. As a general goal, aim for at least 30 minutes of moderate exercise every day.\n Control blood pressure and cholesterol levels:\nMake lifestyle changes and take medications as prescribed to manage high blood pressure (hypertension) or high cholesterol.\n Control stress:\nAvoid unnecessary stress and learn strategies to manage and reduce stress. \n Limit alcohol:\n If you choose to drink alcohol, do so in moderation. For healthy adults, that means up to one drink a day for women and up to two drinks a day for men. \n Some people may need to avoid alcohol entirely. \n Stop smoking:\n If you smoke and can't quit on your own, talk to your health care provider about strategies or programs to help you break a smoking habit.\n Use over-the-counter medications with caution:\n Some cold and cough medications contain stimulants that may increase the heart rate. Always tell your health care provider about the medications you take, including those bought without a prescription."
                          ,anchor=CENTER,background="white",foreground="orange",font=('times', 19, ' bold '))
           yes.pack(padx=0, pady=100)
           yes.place(x=0,y=0)
           
           sqliteConnection = sqlite3.connect('evaluation.db')
           #cursor = sqliteConnection.cursor()
           print("Connected to SQLite")
           
           r_set = sqliteConnection.execute("select * from admin_registration where id =" + str(id) +"");
          #cursor.execute(sql_fetch_blob_query, (id))
           print(r_set)
           i=0
           for row in r_set:
              print("id=",row[0],)
              b=row[0]
              print(b)
              r_set1 = sqliteConnection.execute("select * from admin_registration where id =" + str(b) +"");
              with open(r"report.txt", 'w') as f:
                  for row in r_set1:
                      line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-VEB(Ventricular ectopic beat)"#,row[3],row[4],row[5],row[6]
                      f.write(line)
                      print(row[0],row[1],row[2])
              # for row in r_set1:
              from datetime import date

              today = date.today()
                
              # dd/mm/YY
              d1 = today.strftime("%d/%m/%Y")
              print("d1 =", d1)
              # datetime object containing current date and time
              from datetime import datetime

              now = datetime.now()
                 
              print("now =", now)
              # dd/mm/YY H:M:S
              dt_string = now.strftime("%H:%M:%S")
              print("time =", dt_string)
              Name = row[1]
              address = row[2]
              age = row[7]
              result = 'VEB(Ventricular ectopic beat'
              print(Name,address,age,result)
              conn = sqlite3.connect('evaluation.db')
              with conn:
                  cursor = conn.cursor()
                  cursor.execute(
                      'INSERT INTO record(Username,age,address,result,date,time) VALUES(?,?,?,?,?,?)',
                      (Name,address,age,result,d1,dt_string))

                  conn.commit()
                  #db.close()
            
                    
           
    
        if v[0]=='N':
           print("N(Normal)")
           yes = tk.Label(root,wraplength=1565,text="Your Result :\n (Normal) \n___Precaution___\n * \nThe best ways to prevent tachycardia are to maintain\n a healthy heart and prevent heart disease.\nIf you already have heart disease, monitor it and follow your treatment plan.\n Be sure you understand your treatment plan, and take all medications as prescribed. \n\nTake the following steps to keep the heart healthy:\nEat a balanced, nutritious diet:\n A diet low in saturated and trans fats and rich in fruits, vegetables and whole grains helps keep the heart healthy.\n Exercise and maintain a healthy weight: \nBeing overweight increases the risk of developing heart disease. As a general goal, aim for at least 30 minutes of moderate exercise every day.\n Control blood pressure and cholesterol levels:\nMake lifestyle changes and take medications as prescribed to manage high blood pressure (hypertension) or high cholesterol.\n Control stress:\nAvoid unnecessary stress and learn strategies to manage and reduce stress. \n Limit alcohol:\n If you choose to drink alcohol, do so in moderation. For healthy adults, that means up to one drink a day for women and up to two drinks a day for men. \n Some people may need to avoid alcohol entirely. \n Stop smoking:\n If you smoke and can't quit on your own, talk to your health care provider about strategies or programs to help you break a smoking habit.\n Use over-the-counter medications with caution:\n Some cold and cough medications contain stimulants that may increase the heart rate. Always tell your health care provider about the medications you take, including those bought without a prescription."
                         ,anchor=CENTER,background="white",foreground="orange",font=('times', 19, ' bold '))
           yes.pack(padx=0, pady=100)
           yes.place(x=0,y=0)
           
           sqliteConnection = sqlite3.connect('evaluation.db')
           #cursor = sqliteConnection.cursor()
           print("Connected to SQLite")
           
           r_set = sqliteConnection.execute("select * from admin_registration where id =" + str(id) +"");
          #cursor.execute(sql_fetch_blob_query, (id))
           print(r_set)
           i=0
           for row in r_set:
              print("id=",row[0],)
              b=row[0]
              print(b)
              r_set1 = sqliteConnection.execute("select * from admin_registration where id =" + str(b) +"");
              with open(r"report.txt", 'w') as f:
                  for row in r_set1:
                      line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-VEB(Ventricular ectopic beat)"#,row[3],row[4],row[5],row[6]
                      f.write(line)
                      print(row[0],row[1],row[2])
              # for row in r_set1:
              from datetime import date

              today = date.today()
                
              # dd/mm/YY
              d1 = today.strftime("%d/%m/%Y")
              print("d1 =", d1)
              # datetime object containing current date and time
              from datetime import datetime

              now = datetime.now()
                 
              print("now =", now)
              # dd/mm/YY H:M:S
              dt_string = now.strftime("%H:%M:%S")
              print("time =", dt_string)
              Name = row[1]
              address = row[2]
              age = row[7]
              result = 'N(Normal)'
              print(Name,address,age,result)
              conn = sqlite3.connect('evaluation.db')
              with conn:
                  cursor = conn.cursor()
                  cursor.execute(
                      'INSERT INTO record(Username,age,address,result,date,time) VALUES(?,?,?,?,?,?)',
                      (Name,address,age,result,d1,dt_string))

                  conn.commit()
                  #db.close()
           
        if v[0]=='F':
              print("F (Fusion Beat)")
              yes = tk.Label(root,wraplength=1565,text="Your Result :\n (Fusion Beat) \n___Precaution___\n * \nThe best ways to prevent tachycardia are to maintain\n a healthy heart and prevent heart disease.\nIf you already have heart disease, monitor it and follow your treatment plan.\n Be sure you understand your treatment plan, and take all medications as prescribed. \n\nTake the following steps to keep the heart healthy:\nEat a balanced, nutritious diet:\n A diet low in saturated and trans fats and rich in fruits, vegetables and whole grains helps keep the heart healthy.\n Exercise and maintain a healthy weight: \nBeing overweight increases the risk of developing heart disease. As a general goal, aim for at least 30 minutes of moderate exercise every day.\n Control blood pressure and cholesterol levels:\nMake lifestyle changes and take medications as prescribed to manage high blood pressure (hypertension) or high cholesterol.\n Control stress:\nAvoid unnecessary stress and learn strategies to manage and reduce stress. \n Limit alcohol:\n If you choose to drink alcohol, do so in moderation. For healthy adults, that means up to one drink a day for women and up to two drinks a day for men. \n Some people may need to avoid alcohol entirely. \n Stop smoking:\n If you smoke and can't quit on your own, talk to your health care provider about strategies or programs to help you break a smoking habit.\n Use over-the-counter medications with caution:\n Some cold and cough medications contain stimulants that may increase the heart rate. Always tell your health care provider about the medications you take, including those bought without a prescription."
                             ,anchor=CENTER,background="white",foreground="orange",font=('times', 19, ' bold '))
              yes.pack(padx=0, pady=100)
              yes.place(x=0,y=0)
              
              sqliteConnection = sqlite3.connect('evaluation.db')
              #cursor = sqliteConnection.cursor()
              print("Connected to SQLite")
              
              r_set = sqliteConnection.execute("select * from admin_registration where id =" + str(id) +"");
             #cursor.execute(sql_fetch_blob_query, (id))
              print(r_set)
              i=0
              for row in r_set:
                 print("id=",row[0],)
                 b=row[0]
                 print(b)
                 r_set1 = sqliteConnection.execute("select * from admin_registration where id =" + str(b) +"");
                 with open(r"report.txt", 'w') as f:
                     for row in r_set1:
                         line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-VEB(Ventricular ectopic beat)"#,row[3],row[4],row[5],row[6]
                         f.write(line)
                         print(row[0],row[1],row[2])
                 # for row in r_set1:
                 from datetime import date

                 today = date.today()
                   
                 # dd/mm/YY
                 d1 = today.strftime("%d/%m/%Y")
                 print("d1 =", d1)
                 # datetime object containing current date and time
                 from datetime import datetime

                 now = datetime.now()
                    
                 print("now =", now)
                 # dd/mm/YY H:M:S
                 dt_string = now.strftime("%H:%M:%S")
                 print("time =", dt_string)
                 Name = row[1]
                 address = row[2]
                 age = row[7]
                 result = 'F (Fusion Beat)'
                 print(Name,address,age,result)
                 conn = sqlite3.connect('evaluation.db')
                 with conn:
                     cursor = conn.cursor()
                     cursor.execute(
                         'INSERT INTO record(Username,age,address,result,date,time) VALUES(?,?,?,?,?,?)',
                         (Name,address,age,result,d1,dt_string))

                     conn.commit()
                     #db.close()
      
       
            
       
    l1=tk.Label(root,text="record",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l1.place(x=5,y=10)
    record=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=record)
    record.place(x=500,y=10)

    l2=tk.Label(root,text="preRR",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l2.place(x=5,y=60)
    preRR=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=preRR)
    preRR.place(x=500,y=60)

    l3=tk.Label(root,text="postRR",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l3.place(x=5,y=110)
    postRR=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=postRR)
    postRR.place(x=500,y=110)
    
    
    l4=tk.Label(root,text="pPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l4.place(x=5,y=160)
    pPeak=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=pPeak)
    pPeak.place(x=500,y=160)

    l5=tk.Label(root,text="tPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l5.place(x=5,y=210)
    tPeak=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=tPeak)
    tPeak.place(x=500,y=210)

    l6=tk.Label(root,text="rPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l6.place(x=5,y=260)
    rPeak=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=rPeak)
    rPeak.place(x=500,y=260)
    
    
    l7=tk.Label(root,text="sPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l7.place(x=5,y=310)
    
    sPeak=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=sPeak)
    sPeak.place(x=500,y=310)
    
   

    l8=tk.Label(root,text="qPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l8.place(x=5,y=360)
    qPeak=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=qPeak)
    qPeak.place(x=500,y=360)

    l9=tk.Label(root,text="qrs_interval",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l9.place(x=5,y=410)
    qrs_interval=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=qrs_interval)
    qrs_interval.place(x=500,y=410)

    
    # qrs_interval=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=qPeak)
    # qrs_interval.place(x=500,y=400)
    
    
    # frame_alpr = tk.LabelFrame(root, text="  ", width=750, height=850, bd=5, font=('times', 14, ' bold '),bg="white")
    # frame_alpr.grid(row=0, column=0)
    # frame_alpr.place(x=830, y=0)

    
    
    # logo_label=tk.Label()
    # logo_label.place(x=0,y=55)


   

    button1 = tk.Button(root,text="Submit",command=Detect,bg ="red", fg = "white",font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=610)


    root.mainloop()

Train()