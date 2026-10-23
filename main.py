from tkinter import Tk, StringVar, Label
import button_setup

application = Tk()

application.title("Calculator")
application.geometry("248x314")
application.resizable(False,False)
display_text = StringVar(application)

display = Label(
    application,
    textvariable=display_text,
    font=(".AppleSystemUIFont", 28),
    bg="#1e1e1e",
    fg="white",
    anchor="e",
    padx=10
)

display.grid(row=0, column=0, columnspan=4, sticky="ew", pady=8)

button_setup.setup_buttons(application, display_text)

def report_window_width(event):
    if event.widget is application:
        print(f"Window width: {event.width} pixels")
        print(f"Height{event.height}")

application.bind("<Configure>", report_window_width)

application.mainloop()