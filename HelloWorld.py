#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:17:06 2019

@author: supaul
"""

from tkinter import *
from tkinter import messagebox
import csv
def checkRegularExpression(email):
    if(len(email)>7):
        if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email)!=None):
            return True
        else:
            return False
    else:
        return False
    
def buttonClick():
    eMail=enterText.get()
    if(checkRegularExpression(eMail)):
        messagebox.showinfo("Success", "You have been subscribed to the newsletter")
        with open('EmailList.csv', 'a') as outfile:
            newFileWriter=csv.writer(outfile)
            emailList=[];
            emailList.append(eMail)
            newFileWriter.writerow(emailList)
    else:
        messagebox.showinfo("Failure","Invalid email id")
    return


root=Tk()
root.title("Newsletter")
emailLabel=Label(root,text="E mail")
emailLabel.pack()
enterText = Entry(root)
enterText.pack()
button=Button(root,text="Submit",command=buttonClick)
button.pack()

root.mainloop()

