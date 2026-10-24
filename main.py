from tkinter import *
import button_setup
import functions

application = Tk()

application.title("Calculator")
# application.geometry("248x376")
# application.resizable(False,False)
display_text = StringVar(application)

display = Label(
    application,
    textvariable=display_text,
    font=("System", 28),
    bg="#1e1e1e",
    fg="white",
    anchor="e",
    padx=10
)

display.grid(row=0, column=0, columnspan=4, sticky="ew", pady=8)

# def on_resize(event):
#     print(f"Width: {event.width}, Height: {event.height}")

# application.bind("<Configure>", on_resize)

button_setup.setup_buttons(application, display_text)

application.mainloop()