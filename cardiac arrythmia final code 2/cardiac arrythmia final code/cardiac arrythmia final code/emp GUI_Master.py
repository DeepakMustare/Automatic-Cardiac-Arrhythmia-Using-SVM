from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from mlxtend.plotting import plot_confusion_matrix
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve


root = tk.Tk()
root.title("Classification of Cardiac Arrhythmia Using SVM")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

img=ImageTk.PhotoImage(Image.open("bg3.jpg"))

img2=ImageTk.PhotoImage(Image.open("bg2.jpeg"))

img3=ImageTk.PhotoImage(Image.open("img1.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()
 # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Classification of Cardiac Arrhythmia", font=('times', 35,' bold '), height=1, width=65,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv(r"F:/cardiac arrythmia final code 2/cardiac arrythmia final code/cardiac arrythmia final code/cardiac1.csv")



data = data.dropna()

le = LabelEncoder()
# data['AHD'] = le.fit_transform(data['AHD'])

# data['Thal'] = le.fit_transform(data['Thal'])
# data['ChestPain'] = le.fit_transform(data['ChestPain'])

# data.head()

# """Feature Selection => Manual"""
# x = data.drop(['AHD', 'Series'], axis=1)


def Data_Preprocessing():
    data = pd.read_csv(r"F:/cardiac arrythmia final code 2/cardiac arrythmia final code/cardiac arrythmia final code/cardiac1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""
   
    le = LabelEncoder()
 
    data['record'] = le.fit_transform(data['record'])
    
    data['preRR'] = le.fit_transform(data['preRR']) 
    
    data['postRR'] = le.fit_transform(data['postRR'])

    data['pPeak'] = le.fit_transform(data['pPeak'])
 
    data['tPeak'] = le.fit_transform(data['tPeak'])
 
    data['rPeak'] = le.fit_transform(data['rPeak'])
 
    data['sPeak'] = le.fit_transform(data['sPeak'])
 
    data['qPeak'] = le.fit_transform(data['qPeak'])
 
    data['qrs_interval'] = le.fit_transform(data['qrs_interval'])
    
    data.head()
  
   
  

    """Feature Selection => Manual"""
    x = data.drop(['type'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['type']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=213, y=85)


def Model_Training():
    print('hi')
    data = pd.read_csv(r"F:/cardiac arrythmia final code 2/cardiac arrythmia final code/cardiac arrythmia final code/cardiac1.csv")
    data.head()

    data = data.dropna()


    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['record'] = le.fit_transform(data['record'])
    
    data['preRR'] = le.fit_transform(data['preRR'])
    
    data['postRR'] = le.fit_transform(data['postRR'])

    data['pPeak'] = le.fit_transform(data['pPeak'])
    
    data['tPeak'] = le.fit_transform(data['tPeak'])
    
    data['rPeak'] = le.fit_transform(data['rPeak'])
    
    data['sPeak'] = le.fit_transform(data['sPeak'])
    
    data['qPeak'] = le.fit_transform(data['qPeak'])
    
    data['qrs_interval'] = le.fit_transform(data['qrs_interval'])
   
  
    

    """Feature Selection => Manual"""
    x = data.drop(['type'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['type']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    #from sklearn.naive_bayes import GaussianNB  
    #classifier = GaussianNB()  
    #classifier.fit(x_train, y_train)  

    
    from sklearn.svm import SVC
   
    svcclassifier = SVC(kernel='linear',random_state=0)
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    #y_pred = classifier.predict(x_test)
    #print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix 

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    import seaborn as sns
    rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(y_test,y_pred)
    
    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    plt.title('Reciver Operating Characterstic Curve')
    
    plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Support Vector Machine',color='red')  
    plt.plot([0,1],ls='--',color='blue')
    plt.plot([0,0],[1,0],color='green')
    plt.plot([1,1],color='green')
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.legend()
    plt.show()

    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as card_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"card_MODEL_MODEL.joblib")
    print("Model saved as card_MODEL_MODEL.joblib")



def call_file():
    import Check_Prediction
    Check_Prediction.Train()
   # "F:\cardiac arrythmia final code 2\cardiac arrythmia final code\cardiac arrythmia final code\Check_Prediction.py"


def window():
    root.destroy()

button2 = tk.Button(root, foreground="black", background="pink", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=20, y=90)

button3 = tk.Button(root, foreground="black", background="pink", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training,  width=15, height=2)
button3.place(x=20, y=170)

button4 = tk.Button(root, foreground="black", background="pink", font=("Tempus Sans ITC", 14, "bold"),
                    text="Classification of Cardiac Arrhythmia", command=call_file, width=30, height=2)
button4.place(x=20, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=20, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''