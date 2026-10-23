from tkinter import *
from tkmacosx import Button
import functions

def setup_buttons(application, display_text):
    operator_button_style = {
        "font": (".AppleSystemUIFont", 20, "bold"),
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
        "font": (".AppleSystemUIFont", 20),
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
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
        ("0", 4, 0), (".", 4, 1)
    ]

    # 2. Loop through the layout and generate the buttons automatically
    for digit, r, c in number_layout:
        btn = Button(
            application, 
            text=digit, 
            command=lambda d=digit: functions.number_click(display_text, d),
            **number_button_style
        )
        btn.grid(row=r, column=c, padx=1, pady=1)

    operator_layout = [
        ("÷", 1, 3),
        ("×", 2, 3),
        ("-", 3, 3),
        ("+", 4, 3),
        ("=", 4, 2)
    ]

    for sign, r, c in operator_layout:
        btn = Button(
            application, 
            text=sign, 
            command=lambda s=sign: functions.operator_click(display_text,s),
            **operator_button_style
        )
        btn.grid(row=r, column=c, padx=1, pady=1)