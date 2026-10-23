from tkinter import *
from tkmacosx import Button
import functions


application = Tk()
plus_sign = Button(
    application,
    text="+",
    command=lambda:functions.operator_click("+"),
    font=("Ink Free", 20, "bold"),
    bg="#f29e1f",
    fg="black",
    activebackground="#ffb84d",
    activeforeground="black",
    bordercolor="#222222",
    bd=0,
    focuscolor="",
    width=60,
    height=60,
)
plus_sign.pack()

plus_sign = Button(
    application,
    text="+",
    command=lambda:functions.operator_click("+"),
    font=("Ink Free", 20, "bold"),
    bg="#f29e1f",
    fg="black",
    activebackground="#ffb84d",
    activeforeground="black",
    bordercolor="#222222",
    bd=0,
    focuscolor="",
    width=60,
    height=60,
)
application.title("Calculator")
application.mainloop()