from tkinter import *

# initialize window
window = Tk()

# set window title.
window.title("Cross Roads C A L C U L A T O R E")

# set window dimension.
# window.geometry("400x500")
window.configure(background='black')
# set diplay label.
shintolabel = Entry(window, width=50)
shintolabel.grid(row=0, column=0, columnspan=5)


def button_click(number_click):
    shintolabel.insert(0, number_click)


def button_clr():
    shintolabel.delete(0, END)


def button_divison():
    add = shintolabel.get()
    global addition
    global calc
    calc = "division"
    addition = int(add)
    shintolabel.delete(0, END)


def button_multiplication():
    add = shintolabel.get()
    global addition
    global calc
    calc = "multiplication"
    addition = int(add)
    shintolabel.delete(0, END)


def button_add():
    add = shintolabel.get()
    global addition
    global calc
    calc = "addition"
    addition = int(add)
    shintolabel.delete(0, END)


def button_substraction():
    add = shintolabel.get()
    global addition
    global calc
    calc = "substraction"
    addition = int(add)
    shintolabel.delete(0, END)


def button_equal():
    equal = shintolabel.get()
    shintolabel.delete(0, END)

    if calc == 'division':
        shintolabel.insert(0, addition / int(equal))

    if calc == 'multiplication':
        shintolabel.insert(0, addition * int(equal))

    if calc == 'addition':
        shintolabel.insert(0, addition + int(equal))

    if calc == 'substraction':
        shintolabel.insert(0, addition - int(equal))


shintobtn_c = Button(window, text='C', padx=70, pady=10, command=button_clr)
shintobtn_c.grid(row=1, column=0, columnspan=2)

shintobtn_div = Button(window, text="/", padx=70, pady=10, command=button_divison, bg='red')
shintobtn_div.grid(row=1, column=3, columnspan=2)

# set buttons second row

shintobtn_7 = Button(window, text="7", padx=30, pady=10, command=lambda: button_click(7))
shintobtn_7.grid(row=2, column=0)

shintobtn_8 = Button(window, text="8", padx=30, pady=10, command=lambda: button_click(8))
shintobtn_8.grid(row=2, column=1)

shintobtn_9 = Button(window, text="9", padx=30, pady=10, command=lambda: button_click(9))
shintobtn_9.grid(row=2, column=2, rowspan=1)

shintobtn_str = Button(window, text="*", padx=30, pady=10, command=button_multiplication)
shintobtn_str.grid(row=2, column=3)

# set third raw buttons

shintobtn_4 = Button(window, text="4", padx=30, pady=10, command=lambda: button_click(4))
shintobtn_4.grid(row=3, column=0)

shintobtn_5 = Button(window, text="5", padx=30, pady=10, command=lambda: button_click(5))
shintobtn_5.grid(row=3, column=1)

shintobtn_6 = Button(window, text="6", padx=30, pady=10, command=lambda: button_click(6))
shintobtn_6.grid(row=3, column=2)

shintobtn_mnz = Button(window, text="-", padx=30, pady=10, command=button_substraction)
shintobtn_mnz.grid(row=3, column=3)

# set fourth raw

shintobtn_1 = Button(window, text="1", padx=30, pady=30, command=lambda: button_click(1))
shintobtn_1.grid(row=4, column=0, rowspan=2)

shintobtn_2 = Button(window, text="2", padx=30, pady=10, command=lambda: button_click(2))
shintobtn_2.grid(row=4, column=1)

shintobtn_3 = Button(window, text="3", padx=30, pady=10, command=lambda: button_click(3))
shintobtn_3.grid(row=4, column=2)

shintobtn_plz = Button(window, text="+", padx=30, pady=10, command=button_add)
shintobtn_plz.grid(row=4, column=3)

# set fifth raw

shintobtn_zro = Button(window, text="0", padx=30, pady=10, command=lambda: button_click(0))
shintobtn_zro.grid(row=5, column=1, columnspan=1)

shintobtn_dt = Button(window, text=".", padx=30, pady=10, command=lambda: button_click('.'))
shintobtn_dt.grid(row=5, column=2)

shintobtn_equal = Button(window, text="=", padx=30, pady=10, command=button_equal)
shintobtn_equal.grid(row=5, column=3)

window.mainloop()
