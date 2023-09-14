from tkinter import *

bgcolor = "#0E2954"
textcolor = "#F39F5A"
textboxbg = "#1F6E8C"

count = 10

idle = True

def set_idle():
    global idle
    idle = True
    window.after(1000, countdown)

def set_active(event):
    global idle, count, idle_id
    idle = False
    count = 10
    timer_var.set(count)
    try:
        window.after_cancel(idle_id)
    except UnboundLocalError:
        pass
    except ValueError:
        pass
    idle_id = window.after(1000, set_idle)

def countdown():
    global count, idle
    if idle and count > 0:
        count -= 1
        timer_var.set(count)
        window.after(1000, countdown)
    if count == 0:
        text_box.delete("1.0", END)
        timer_var.set("Oops...")

window = Tk()
window.geometry("1000x1000")
window.title("Quick, think of something!")
window.config(bg=bgcolor)

text_box = Text(window,
                font="Consolas,50",
                height=40, 
                width=80, 
                background=textboxbg,
                fg=textcolor, 
                relief="groove", 
                bd=5)
text_box.pack(expand=True)
text_box.bind("<KeyRelease>", set_active)

warning_label = Label(window,
                      text="Your efforts will be futile in...",
                      bg=bgcolor,
                      fg=textcolor)
warning_label.pack()

timer_var = StringVar()
timer_var.set(count)
timer_label = Label(window, 
                    textvariable=timer_var, 
                    font="Consolas, 80", 
                    bg=bgcolor, 
                    fg=textcolor)
timer_label.pack(pady=(0,20))

idle_id = window.after(1000, countdown)

window.mainloop()