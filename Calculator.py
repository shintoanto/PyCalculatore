from tkinter import *

# initialize window
window = Tk()

# set window title.
window.title("Cross Roads C A L C U L A T O R E")

# set window dimension.
window.geometry("400x500")

# set diplay label.
shintolabel = Entry(window, text='This is a example window frame test', width='50').place(x=0, y=150)

# set button.
# creating a button instance and placing the button on my window
shintobtn = Button(window, text="Quit").place(x=0, y=0)

window.mainloop()
