from tkinter import *
from tkmacosx import Button
import buttons

calculator_screen = Label()
calculator_screen.pack()

application = Tk()

application.title("Calculator")

buttons.setup_buttons(application)

application.mainloop()