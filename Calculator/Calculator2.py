# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:57:04 2022

@author: Cereg Marin
"""

"""
LIBRARY
"""
import tkinter as tk

"""
INIT PHASE
"""
calculation = ""
"""
FUNCTIONS
"""
def AddToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def Calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        text_result.delete(1.0,"end")
        text_result.insert(1.0,"error") 

def Clear():
    global calculation
    calculation = " "
    text_result.delete(1.0,"end")
    text_result.insert(1.0,"") 

def ShowFunction():
    pass

"""
GUI
"""

root = tk.Tk()
root.geometry("540x300")
root.config(bg='#9FD996')

text_result = tk.Text(root, height=1,width=29,font=("Arial",24))
text_result.grid(columnspan=10)

btn1 = tk.Button(root,text="1", command= lambda:AddToCalculation(1),width =7, font="Arial")
btn1.grid(row =2, column =1)

btn2 = tk.Button(root,text="2", command= lambda:AddToCalculation(2),width =7, font="Arial")
btn2.grid(row = 2, column =2)

btn3 = tk.Button(root,text="3", command= lambda:AddToCalculation(3),width =7, font="Arial")
btn3.grid(row = 2, column =3)

btn4 = tk.Button(root,text="4", command= lambda:AddToCalculation(4),width =7, font="Arial")
btn4.grid(row = 3, column =1)

btn5 = tk.Button(root,text="5", command= lambda:AddToCalculation(5),width =7, font="Arial")
btn5.grid(row = 3, column =2)

btn6 = tk.Button(root,text="6", command= lambda:AddToCalculation(6),width =7, font="Arial")
btn6.grid(row = 3, column =3)

btn7 = tk.Button(root,text="7", command= lambda:AddToCalculation(7),width =7, font="Arial")
btn7.grid(row = 4, column =1)

btn8 = tk.Button(root,text="8", command= lambda:AddToCalculation(8),width =7, font="Arial")
btn8.grid(row = 4, column =2)

btn9 = tk.Button(root,text="9", command= lambda:AddToCalculation(9),width =7, font="Arial")
btn9.grid(row = 4, column =3)

btn0 = tk.Button(root,text="0", command= lambda:AddToCalculation(0),width =7, font="Arial")
btn0.grid(row = 5, column =2)

btnCalculate = tk.Button(root,text="=", command= Calculate ,width =25, font="Arial")
btnCalculate.grid(row = 6, columnspan =5)

label = tk.Label(root,text="",height =1)
label.grid(row = 1, column =4)

label2 = tk.Label(root,text="",height =2)
label2.grid(row = 2, column =4)

label3 = tk.Label(root,text="",height =2)
label3.grid(row = 3, column =4)

label4 = tk.Label(root,text="",height =2)
label4.grid(row = 4, column =4)

label5 = tk.Label(root,text="",height =2)
label5.grid(row = 5, column =4)

btnclr = tk.Button(root,text="CLR", command= Clear ,width =7, font="Arial")
btnclr.grid(row = 2, column =6)

btnplus = tk.Button(root,text="+", command= lambda:AddToCalculation("+"),width =7, font="Arial")
btnplus.grid(row = 3, column =5)

btnminus = tk.Button(root,text="-", command= lambda:AddToCalculation("-"),width =7, font="Arial")
btnminus.grid(row = 3, column =6)

btmul = tk.Button(root,text="*", command= lambda:AddToCalculation("*"),width =7, font="Arial")
btmul.grid(row = 3, column =7)

btdiv = tk.Button(root,text="/", command= lambda:AddToCalculation("/"),width =7, font="Arial")
btdiv.grid(row = 3, column =8)








root.mainloop()

