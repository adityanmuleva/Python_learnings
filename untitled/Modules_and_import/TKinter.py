"""
import tkinter
mainwindow = tkinter.Tk()

mainwindow.title("My python window")
mainwindow.geometry('640x480')

label = tkinter.Label(mainwindow, text="Hello world")
label.pack(side='top')

leftframe= tkinter.Frame(mainwindow)
leftframe.pack(side='left', anchor='n',fill=tkinter.Y,expand=False)

canvas = tkinter.Canvas(mainwindow,relief="raised",borderwidth=3)
canvas.pack(side='left')

rightframe = tkinter.Frame(mainwindow)
rightframe.pack(side='right', expand=True)
button1 = tkinter.Button(mainwindow,text="button1", borderwidth="1")
button2 = tkinter.Button(mainwindow,text="button2", borderwidth="2")
button3 = tkinter.Button(mainwindow,text="button3", borderwidth="3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainwindow.mainloop()
"""

"""
import tkinter
mainwindow = tkinter.Tk()
mainwindow.title("Hello! Demo")
mainwindow.geometry("680x420-1-20")

label = tkinter.Label(mainwindow, text="aaditya muleva")
label.grid(row=0, column=0)

leftframe = tkinter.Frame(mainwindow)
leftframe.grid(row=1, column=1)
canvas = tkinter.Canvas(leftframe, relief="raised", borderwidth=4)
canvas.grid(row=1, column=1)

rightframe = tkinter.Frame(mainwindow)
rightframe.grid(row=1, column=2)
button1 = tkinter.Button(rightframe, text="button1", borderwidth=1)
button2 = tkinter.Button(rightframe, text="button2", borderwidth=2)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)

mainwindow.mainloop()
"""
# ADVANCED TKINTER 1

import tkinter
import os

mainwindow = tkinter.Tk()
mainwindow.title("Test advance")
mainwindow.geometry("620x480-4-200")

label = tkinter.Label(mainwindow, text="Test Advance")
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=3)
mainwindow.columnconfigure(3, weight=3)
mainwindow.columnconfigure(4, weight=3)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1, column=0, sticky="nsew", rowspan=2)
filelist.config(border=2, relief="sunken")

for zone in os.listdir("C:\Windows\System32"):
    filelist.insert(tkinter.END, zone)

scrollbar1= tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=filelist.yview)
scrollbar1.grid(row=1, column=1, sticky="nsw", rowspan=2)
filelist["yscrollcommand"] = scrollbar1.set

scrollbar2 = tkinter.Scrollbar(mainwindow, orient=tkinter.HORIZONTAL, command=filelist.xview)
scrollbar2.grid(row=3, column=0, sticky="new", rowspan=2)
filelist["xscrollcommand"] = scrollbar2.set

optionframe = tkinter.LabelFrame(mainwindow, text="File Name")
optionframe.grid(row=1, column=2, sticky="ne")

rbvalue = tkinter.IntVar()
rbvalue.set(0)

radio1 = tkinter.Radiobutton(optionframe, text="File Name", value=1, variable=rbvalue)
radio2 = tkinter.Radiobutton(optionframe, text="Path", value=2, variable=rbvalue)
radio3 = tkinter.Radiobutton(optionframe, text="Time Stamp", value=3, variable=rbvalue)
radio1.grid(row=0, column=0, sticky="w")
radio2.grid(row=1, column=0, sticky="w")
radio3.grid(row=2, column=0, sticky="w")

resultlabel = tkinter.Label(mainwindow, text="Result")
resultlabel.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(mainwindow)
result.grid(row=2,column=2,sticky="sw")

timeframe = tkinter.LabelFrame(mainwindow, text="Time")
timeframe.grid(row=3, column=0,sticky="new")
hourspinner = tkinter.Spinbox(timeframe, width=2, value=tuple(range(0,24)))
minutespinner = tkinter.Spinbox(timeframe, width=2, from_=0,to=59)
secondspinner = tkinter.Spinbox(timeframe, width =2, from_=0, to=59)
hourspinner.grid(row=0, column=0)
tkinter.Label(timeframe,text=":").grid(row=0,column=1)
minutespinner.grid(row=0,column=2)
tkinter.Label(timeframe,text=":").grid(row=0,column=3)
secondspinner.grid(row=0,column=4)

OKbutton = tkinter.Button(mainwindow, text="OK", width=4)
OKbutton.grid(row=3,column=3,sticky="es")

Cancelbutton = tkinter.Button(mainwindow, text="CANCEL", width=7, command=mainwindow.quit)
Cancelbutton.grid(row=3,column=4,sticky="ws")

timeframe["padx"] = 36
mainwindow["padx"] = 36
mainwindow.mainloop()
print(rbvalue.get())