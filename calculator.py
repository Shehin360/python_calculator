from tkinter import *
window = Tk() #create object window
window.title("Calculator")

entry = Entry(window,width=20,justify=RIGHT)
entry.grid(row=0,column=0,columnspan=4)

expression =""
def button_click(value):
    global expression
    expression=expression+str(value)
    entry.delete(0,END)
    entry.insert(END,expression)


def button_clear():
    global expression
    expression=""
    entry.delete(0,END)



# Number buttons
button1 = Button(window, text="1", width=5, height=2, command=lambda: button_click("1"))
button1.grid(row=1, column=0)

button2 = Button(window, text="2", width=5, height=2, command=lambda: button_click("2"))
button2.grid(row=1, column=1)

button3 = Button(window, text="3", width=5, height=2, command=lambda: button_click("3"))
button3.grid(row=1, column=2)

button4 = Button(window, text="4", width=5, height=2, command=lambda: button_click("4"))
button4.grid(row=2, column=0)

button5 = Button(window, text="5", width=5, height=2, command=lambda: button_click("5"))
button5.grid(row=2, column=1)

button6 = Button(window, text="6", width=5, height=2, command=lambda: button_click("6"))
button6.grid(row=2, column=2)

button7 = Button(window, text="7", width=5, height=2, command=lambda: button_click("7"))
button7.grid(row=3, column=0)

button8 = Button(window, text="8", width=5, height=2, command=lambda: button_click("8"))
button8.grid(row=3, column=1)

button9 = Button(window, text="9", width=5, height=2, command=lambda: button_click("9"))
button9.grid(row=3, column=2)

button0 = Button(window, text="0", width=5, height=2, command=lambda: button_click("0"))
button0.grid(row=4, column=1)

#operators start here :------------------------------------------------------------------------------------------------------------
button_plus = Button(window, text="+", width=5, height=2, command=lambda: button_click("+"))
button_plus.grid(row=1, column=3)

button_minus = Button(window, text="-", width=5, height=2, command=lambda: button_click("-"))
button_minus.grid(row=2, column=3)

button_mul = Button(window, text="*", width=5, height=2, command=lambda: button_click("*"))
button_mul.grid(row=3, column=3)

button_div = Button(window, text="/", width=5, height=2, command=lambda: button_click("/"))
button_div.grid(row=4, column=3)

button_eq = Button(window, text="=", width=5, height=2)
button_eq.grid(row=4, column=2)

button_clear = Button(window,text="C",width=5,height=2, command=lambda: button_clear)
button_clear.grid(row=4,column=0)





label=Label(window,text=":)")



window.mainloop() #looping the window
