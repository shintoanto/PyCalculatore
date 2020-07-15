from tkinter import *

# initialize window
window = Tk()

# set window title.
window.title("Cross Roads C A L C U L A T O R E")

# set window dimension.
#window.geometry("400x500")

# set diplay label.
shintolabel = Entry(window)
shintolabel.grid(row=0, column=0)

# set buttons first row

shintobtn = Button(window, text="C")
shintobtn.grid(row=1, column=0)

shintobtn = Button(window, text="Correct")
shintobtn.grid(row=1, column=1)

shintobtn = Button(window, text="%")
shintobtn.grid(row=1, column=2)

shintobtn = Button(window, text="/")
shintobtn.grid(row=1, column=3)

# set buttons second row

shintobtn = Button(window, text="7")
shintobtn.grid(row=2, column=0)

shintobtn = Button(window, text="8")
shintobtn.grid(row=2, column=1)

shintobtn = Button(window, text="9")
shintobtn.grid(row=2, column=2)

shintobtn = Button(window, text="*")
shintobtn.grid(row=2, column=3)

# set third raw buttons

shintobtn = Button(window, text="4")
shintobtn.grid(row=3, column=0)

shintobtn = Button(window, text="5")
shintobtn.grid(row=3, column=1)

shintobtn = Button(window, text="6")
shintobtn.grid(row=3, column=2)

shintobtn = Button(window, text="-")
shintobtn.grid(row=3, column=3)

# set fourth raw

shintobtn = Button(window, text="1")
shintobtn.grid(row=4, column=0)

shintobtn = Button(window, text="2")
shintobtn.grid(row=4, column=1)

shintobtn = Button(window, text="3")
shintobtn.grid(row=4, column=2)

shintobtn = Button(window, text="+")
shintobtn.grid(row=4, column=3)

# set fifth raw

shintobtn = Button(window, text="_")
shintobtn.grid(row=5, column=0)

shintobtn = Button(window, text="0")
shintobtn.grid(row=5, column=1)

shintobtn = Button(window, text=".")
shintobtn.grid(row=5, column=2)

shintobtn = Button(window, text="=")
shintobtn.grid(row=5, column=3)
window.mainloop()
