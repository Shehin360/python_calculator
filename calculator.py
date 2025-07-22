from tkinter import *
window = Tk() #create object window
window.title("Calculator")




button1=Button(text="1",width="5",height="2")

button1.grid(row=0,column=0)

button2=Button(text="2",width="5",height="2")

button2.grid(row=0,column=1)

button3=Button(text="3",width="5",height="2")

button3.grid(row=0,column=2)

button4=Button(text="4",width="5",height="2")

button4.grid(row=0,column=3)

button5=Button(text="5",width="5",height="2")

button5.grid(row=0,column=4)

button6=Button(text="6",width="5",height="2")

button6.grid(row=1,column=0)

button7=Button(text="7",width="5",height="2")

button7.grid(row=1,column=1)

button8=Button(text="8",width="5",height="2")

button8.grid(row=1,column=2)
             
button9=Button(text="9",width="5",height="2")

button9.grid(row=1,column=3)

button10=Button(text="10",width="5",height="2")

button10.grid(row=1,column=4)





label=Label(window,text=":)")



window.mainloop() #looping the window
