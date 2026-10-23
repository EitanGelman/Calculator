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
        "bordercolor": "#1E1E1E",
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
        "bordercolor": "#1E1E1E",
        "bd": 0,
        "focuscolor": "",
        "width": 60,
        "height": 60,
        "cursor":"hand2"
        
    }

    # 1. Define the grid layout for numbers 1 to 9
    number_layout = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2)
    ]

    # 2. Loop through the layout and generate the buttons automatically
    for digit, r, c in number_layout:
        btn = Button(
            application, 
            text=digit, 
            command=lambda d=digit: functions.number_click(d),  # Advanced lambda binding
            **number_button_style
        )
        btn.grid(row=r, column=c, padx=1, pady=1)


    plus_sign = Button(application,text="+",command=lambda:functions.operator_click("+"),**operator_button_style)
    plus_sign.grid(row=3,column=3,padx=1,pady=1)

    minus_sign = Button(application,text='-',command=lambda:functions.operator_click("-"),**operator_button_style)
    minus_sign.grid(row=2,column=3,padx=1,pady=1)

    mulitplication_sign = Button(application,text="x",command=lambda:functions.operator_click("*"),**operator_button_style)
    mulitplication_sign.grid(row=1,column=3,padx=1,pady=1)

    division_sign = Button(application,text="/",command=lambda:functions.operator_click("/"),**operator_button_style)
    division_sign.grid(row=0,column=3,padx=1,pady=1)

    # one = Button(application,text="1",command=lambda:functions.number_click("1"),**number_button_style)
    # one.grid(row=3,column=0,padx=1,pady=1)

    # two = Button(application,text="2",command=lambda:functions.number_click("2"),**number_button_style)
    # two.grid(row=3,column=1,padx=1,pady=1)

    # three = Button(application,text="3",command=lambda:functions.number_click("3"),**number_button_style)
    # three.grid(row=3,column=2,padx=1,pady=1)

    # four = Button(application,text="4",command=lambda:functions.number_click("4"),**number_button_style)
    # four.grid(row=2,column=0,padx=1,pady=1)

    # five = Button(application,text="5",command=lambda:functions.number_click("5"),**number_button_style)
    # five.grid(row=2,column=1,padx=1,pady=1)

    # six = Button(application,text="6",command=lambda:functions.number_click("6"),**number_button_style)
    # six.grid(row=3,column=2,padx=1,pady=1)