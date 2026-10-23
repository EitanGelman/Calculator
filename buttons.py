from tkinter import *
from tkmacosx import Button
import functions

def setup_buttons(application):
    operator_button_style = {
        "font": ("Ink Free", 20, "bold"),
        "bg": "#f29e1f",
        "fg": "black",
        "activebackground": "#ffb84d",
        "activeforeground": "black",
        "bordercolor": "#222222",
        "bd": 0,
        "focuscolor": "",
        "width": 60,
        "height": 60,
        "cursor":"hand2"
    }

    number_button_style = {
        
    }

    plus_sign = Button(application,text="+",command=lambda:functions.operator_click("+"),**operator_button_style)
    plus_sign.pack()

    minus_sign = Button(application,text='-',command=lambda:functions.operator_click("-"),**operator_button_style)
    minus_sign.pack()

    mulitplication_sign = Button(application,text="x",command=lambda:functions.operator_click("*"),**operator_button_style)
    mulitplication_sign.pack()

    division_sign = Button(application,text="/",command=lambda:functions.operator_click("/"),**operator_button_style)
    division_sign.pack()