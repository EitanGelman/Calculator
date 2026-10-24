from tkinter import *

a = None
n = None
are_these_the_results = False

def clear_display(display_text):
    display_text.set("")

def operator_click(display_text, n):
    global a
    global are_these_the_results
    if n == "+":
        current = float(display_text.get())
        clear_display(display_text)

        if are_these_the_results:
            a = current
        elif a is None:
            a = current
        else:
            a += current

        are_these_the_results = False
        clear_display(display_text)
        
    if n == "=":
        b = float(display_text.get())
        sum = a+b
        clear_display(display_text)
        display_text.set(sum)
        are_these_the_results = True

def number_click(display_text, n):
    global a
    global are_these_the_results

    if are_these_the_results:
        a = None
        are_these_the_results = False
        clear_display(display_text)

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