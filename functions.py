from tkinter import *

a = None
b = None
n = None

def clear_display(display_text):
    display_text.set("")

def operator_click(display_text, n):
    global a
    global b
    if n == "+":
        a = float(display_text.get())
        clear_display(display_text)

    if n == "=":
        
        b = float(display_text.get())
        sum = a+b
        clear_display(display_text)
        display_text.set(sum)

    
def number_click(display_text, n):
    current = display_text.get()

    if n == "." and "." in current:
        return

    display_text.set(current + n)

def extra_func_click(display_text, button_label):
    global a
    global b

    if button_label == "C":
        clear_display(display_text)
    elif button_label == "AC":
        a = None
        b = None
        clear_display(display_text)