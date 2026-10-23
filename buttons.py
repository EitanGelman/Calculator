from tkinter import *
from tkmacosx import Button
import functions

def setup_buttons(application):
    operator_button_style = {
        "font": ("Ink Free", 20, "bold"),
        "bg": "#f29e1f",
        "fg": "black",
        "activebackground": "#ffb84d",
        "activeforeground": "white",
        "bordercolor": "#222222",
        "bd": 0,
        "focuscolor": "",
        "width": 60,
        "height": 60,
        "cursor":"hand2"
    }

    number_button_style = {
        "font": ("Ink Free", 20, "bold"),
        "bg": "black",
        "fg": "white",
        "activebackground": "#1f1f1f",
        "activeforeground": "white",
        "bordercolor": "#222222",
        "bd": 0,
        "focuscolor": "",
        "width": 60,
        "height": 60,
        "cursor":"hand2"
        
    }

    plus_sign = Button(application,text="+",command=lambda:functions.operator_click("+"),**operator_button_style)
    plus_sign.grid(row=3,column=3,padx=2,pady=2)

    minus_sign = Button(application,text='-',command=lambda:functions.operator_click("-"),**operator_button_style)
    minus_sign.grid(row=2,column=3,padx=2,pady=2)

    mulitplication_sign = Button(application,text="x",command=lambda:functions.operator_click("*"),**operator_button_style)
    mulitplication_sign.grid(row=1,column=3,padx=2,pady=2)

    division_sign = Button(application,text="/",command=lambda:functions.operator_click("/"),**operator_button_style)
    division_sign.grid(row=0,column=3,padx=2,pady=2)

    one = Button(application,text="1",command=lambda:functions.number_click("1"),**number_button_style)
    one.grid(row=3,column=0,padx=2,pady=2)

    two = Button(application,text="2",command=lambda:functions.number_click("2"),**number_button_style)
    two.grid(row=3,column=1,padx=2,pady=2)

    three = Button(application,text="3",command=lambda:functions.number_click("3"),**number_button_style)
    three.grid(row=3,column=0,padx=2,pady=2)
