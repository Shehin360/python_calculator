from tkinter import *
window = Tk() #create object window
window.title("Calculator")


# def add():




button1=Button(text="1",width="5",height="2")

button1.grid(row=0,column=0)

button2=Button(text="2",width="5",height="2")

button2.grid(row=0,column=1)

button3=Button(text="3",width="5",height="2")

button3.grid(row=0,column=2)

button4=Button(text="4",width="5",height="2")

button4.grid(row=1,column=0)

button5=Button(text="5",width="5",height="2")

button5.grid(row=1,column=1)

button6=Button(text="6",width="5",height="2")

button6.grid(row=1,column=2)

button7=Button(text="7",width="5",height="2")

button7.grid(row=2,column=0)

button8=Button(text="8",width="5",height="2")

button8.grid(row=2,column=1)
             
button9=Button(text="9",width="5",height="2")

button9.grid(row=2,column=2)

#operators start here :------------------------------------------------------------------------------------------------------------
button_plus = Button(text="+", width="5", height="2")
button_plus.grid(row=0, column=3)

button_minus = Button(text="-", width="5", height="2")
button_minus.grid(row=1, column=3)

button_mul = Button(text="*", width="5", height="2")
button_mul.grid(row=2, column=3)

button_div = Button(text="/", width="5", height="2")
button_div.grid(row=3, column=3)

button_eq = Button(text="=", width="5", height="2")
button_eq.grid(row=3, column=2)

button0 = Button(text="0", width="5", height="2")
button0.grid(row=3, column=1)





label=Label(window,text=":)")



window.mainloop() #looping the window
