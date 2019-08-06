import tkinter

mainwindow = tkinter.Tk()
mainwindow.title("Calculator Demo")
mainwindow.geometry("620x480-4-200")
mainwindow["padx"] = 30
mainwindow["pady"] = 30



TextDisplay = tkinter.Entry(mainwindow)
TextDisplay.grid(row=0, column=0, sticky="nsew")

keypad = tkinter.Frame(mainwindow)
keypad.grid(row=1,column=0)
buttonC = tkinter.Button(keypad,text="C", borderwidth="2")
buttonCE = tkinter.Button(keypad,text="CE", borderwidth="2")
button7 = tkinter.Button(keypad,text="7", borderwidth="2")
button8 = tkinter.Button(keypad,text="8", borderwidth="2")
button9 = tkinter.Button(keypad,text="9", borderwidth="2")
button_plus = tkinter.Button(keypad,text="+", borderwidth="2")
button4 = tkinter.Button(keypad,text="4", borderwidth="2")
button5 = tkinter.Button(keypad,text="5", borderwidth="2")
button6 = tkinter.Button(keypad,text="6", borderwidth="2")
button_minus = tkinter.Button(keypad,text="-", borderwidth="2")
button1 = tkinter.Button(keypad,text="1", borderwidth="2")
button2 = tkinter.Button(keypad,text="2", borderwidth="2")
button3 = tkinter.Button(keypad,text="3", borderwidth="2")
button_multiply = tkinter.Button(keypad,text="*", borderwidth="2")
button0 = tkinter.Button(keypad,text="0", borderwidth="2")
button_equlas = tkinter.Button(keypad,text="=", borderwidth="2")
button_divide = tkinter.Button(keypad,text="/", borderwidth="2")

buttonC.grid(row=1,column=0,sticky="wens")
buttonCE.grid(row=1,column=1,sticky="wens")
button7.grid(row=2,column=0,sticky="wens")
button8.grid(row=2, column=1,sticky="wens")
button9.grid(row=2,column=2,sticky="wens")
button_plus.grid(row=2,column=3,sticky="wens")
button4.grid(row=3,column=0,sticky="wens")
button5.grid(row=3,column=1,sticky="wens")
button6.grid(row=3,column=2,sticky="wens")
button_minus.grid(row=3,column=3,sticky="wens")
button1.grid(row=4,column=0,sticky="wens")
button2.grid(row=4,column=1,sticky="wens")
button3.grid(row=4,column=2,sticky="wens")
button_multiply.grid(row=4,column=3,sticky="wens")
button0.grid(row=5,column=0,sticky="wens")
button_equlas.grid(row=5,column=1,sticky="wens")
button_divide.grid(row=5,column=3,sticky="wens")


mainwindow.mainloop()
