from tkinter import *
from tkmacosx import Button
import buttons


application = Tk()

application.title("Calculator")

buttons.setup_buttons(application)

application.mainloop()