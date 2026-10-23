from tkinter import *
from tkmacosx import Button
import functions


def setup_buttons(application, display_text):
    operator_button_style = {
        "font": ("System", 20, "bold"),
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
        "font": ("System", 20),
        "bg": "#424242",
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

    extra_func_style = {
        "font": ("System", 20),
        "bg": "#9e9e9e",
        "fg": "white",
        "activebackground": "#1f1f1f",
        "activeforeground": "white",                 "bordercolor": "#1E1E1E",
        "bd": 0,
        "focuscolor": "",
        "width": 60,
        "height": 60,
        "cursor":"hand2"
    }

    number_layout = [
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
        ("0", 5, 0), ("00", 5, 1), (".", 5, 2)
    ]

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
        ("=", 5, 3)
    ]

    for sign, r, c in operator_layout:
        btn = Button(
            application, 
            text=sign, 
            command=lambda s=sign: functions.operator_click(display_text,s),
            **operator_button_style
        )
        btn.grid(row=r, column=c, padx=1, pady=1)

    extra_functions_layout = [
        ("⌫", 1, 0),
        ("AC", 1, 1),
        ("%", 1, 2)
    ]

    ac_button = None

    for func, r, c in extra_functions_layout:
            btn = Button(
                application, 
                text=func, 
                command=lambda f=func: functions.extra_func_click(display_text,f),
                **extra_func_style
            )
            if func == "AC":
                 ac_button = btn
            btn.grid(row=r, column=c, padx=1, pady=1)

    ac_button.config(
         command=lambda: functions.extra_func_click(
              display_text, ac_button.cget("text")
         )
    )
    display_text.trace_add(
         "write",
         lambda *_: ac_button.config(
              text="C" if display_text.get() else "AC"
         )
    )