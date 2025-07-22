from tkinter import *
window = Tk() #create object window
window.title("Calculator")
window.geometry("400x500")
window.resizable(False, False)

# Load the image (use PNG or GIF for PhotoImage)
bg_image = PhotoImage(file="pexels-eberhardgross-2310713.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configure grid weights for centering and filling
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

entry = Entry(window, width=20, justify=RIGHT, font=("Arial", 20), state="disabled", disabledforeground="white", disabledbackground="black")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

expression =""

     
def button_click(value):
    global expression
    expression=expression+str(value)
    entry.config(state="normal")
    entry.delete(0,END)
    entry.insert(END,expression)
    entry.config(state="disabled")

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        entry.config(state="normal")
        entry.delete(0, END)
        entry.insert(END, result)
        entry.config(state="disabled")
        expression = result  # allow further calculations
    except Exception:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""


def button_clear():
    global expression
    expression=""
    entry.config(state="normal")
    entry.delete(0,END)
    entry.config(state="disabled")

# Number buttons ---------------------------------------------------------------------------------------------------------


button1 = Button(window, text="1", font=("Arial", 16), command=lambda: button_click("1"))
button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

button2 = Button(window, text="2", font=("Arial", 16), command=lambda: button_click("2"))
button2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

button3 = Button(window, text="3", font=("Arial", 16), command=lambda: button_click("3"))
button3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

button4 = Button(window, text="4", font=("Arial", 16), command=lambda: button_click("4"))
button4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button5 = Button(window, text="5", font=("Arial", 16), command=lambda: button_click("5"))
button5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

button6 = Button(window, text="6", font=("Arial", 16), command=lambda: button_click("6"))
button6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button7 = Button(window, text="7", font=("Arial", 16), command=lambda: button_click("7"))
button7.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button8 = Button(window, text="8", font=("Arial", 16), command=lambda: button_click("8"))
button8.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

button9 = Button(window, text="9", font=("Arial", 16), command=lambda: button_click("9"))
button9.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button0 = Button(window, text="0", font=("Arial", 16), command=lambda: button_click("0"))
button0.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

#operators start here :------------------------------------------------------------------------------------------------------------


button_plus = Button(window, text="+", font=("Arial", 16), command=lambda: button_click("+"))
button_plus.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

button_minus = Button(window, text="-", font=("Arial", 16), command=lambda: button_click("-"))
button_minus.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

button_mul = Button(window, text="*", font=("Arial", 16), command=lambda: button_click("*"))
button_mul.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

button_div = Button(window, text="/", font=("Arial", 16), command=lambda: button_click("/"))
button_div.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

button_eq = Button(window, text="=", font=("Arial", 16), command=button_equal)
button_eq.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

button_clear = Button(window,text="C", font=("Arial", 16), command=button_clear)
button_clear.grid(row=4,column=0, padx=5, pady=5, sticky="nsew")

label=Label(window,text=":)")


window.mainloop() #looping the window
