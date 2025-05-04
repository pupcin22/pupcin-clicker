from tkinter import *
import time
from tkinter import ttk
import tkinter as tk
import json

SAVE_FILE = "clicker_save.json"

# Нова функція форматування чисел (замість humanize)
def format_number(n):
    suffixes = [
        (10**100, 'G'),   # Googol
        (10**63, 'Vg'),   # Vigintillion
        (10**60, 'Nd'),
        (10**57, 'Od'),
        (10**54, 'Sd'),
        (10**51, 'Sxd'),
        (10**48, 'Qd'),
        (10**45, 'Qtd'),
        (10**42, 'Td'),
        (10**39, 'Dd'),
        (10**36, 'Ud'),
        (10**33, 'Dc'),
        (10**30, 'No'),
        (10**27, 'Oc'),
        (10**24, 'Sp'),
        (10**21, 'Sx'),
        (10**18, 'Qi'),
        (10**15, 'Qa'),
        (10**12, 'T'),
        (10**9, 'B'),
        (10**6, 'M'),
        (10**3, 'K')
    ]
    for value, suffix in suffixes:
        if n >= value:
            return f"{n / value:.2f}{suffix}"
    return str(n)

def save_progress():
    data = {
        "click": click,
        "clickpers": clickpers,
        "clickpower": clickpower,
        "value": value,
        "value2": value2,
        "value3": value3,
        "value4": value4,
        "mult": mult,
        "plusclickpers": plusclickpers,
        "krebirth": krebirth
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_progress():
    global click, clickpers, clickpower, value, value2, value3, value4, mult, plusclickpers, krebirth
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            click = data.get("click", 0)
            clickpers = data.get("clickpers", 0)
            clickpower = data.get("clickpower", 1)
            value = data.get("value", 10)
            value2 = data.get("value2", 50)
            value3 = data.get("value3", 1000)
            value4 = data.get("value4", 100)
            mult = data.get("mult", 2)
            plusclickpers = data.get("plusclickpers", 1)
            krebirth = data.get("krebirth", 0)
            buy1["text"] = f"+{plusclickpers} click per second: {format_number(value)}"
            buy2["text"] = f"+1 click power: {format_number(value2)}"
            buy3["text"] = f"double click per second: {format_number(value3)}"
            rebirth["text"] = f"rebirth: {format_number(value4)}"
            widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
            clickcount["text"] = f"{format_number(click)} clicks"
    except FileNotFoundError:
        pass
def reset_game():
    global click, clickpers, clickpower_bonus, clickpower
    global value, value2, value3, value4, mult, plusclickpers, krebirth

    click = 0
    clickpers = 0
    clickpower_bonus = 0
    clickpower = 1
    value = 10
    value2 = 50
    value3 = 1000
    value4 = 100
    mult = 2
    plusclickpers = 1
    krebirth = 0

    save_progress()
    buy1["text"] = f"+{plusclickpers} click per second: {format_number(value)}"
    buy2["text"] = f"+1 click power: {format_number(value2)}"
    buy3["text"] = f"double click per second: {format_number(value3)}"
    rebirth["text"] = f"rebirth: {format_number(value4)}"
    widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    clickcount["text"] = f"{format_number(click)} clicks"
    show_notice("Game reset!")

def auto_save():
    save_progress()
    root.after(5000, auto_save)

root = Tk()
notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook, bg='#077A7D') 
tab2 = tk.Frame(notebook, bg='#077A7D')

notebook.add(tab1, text='clicker')
notebook.add(tab2, text='pursaches')
notebook.pack(expand=True, fill='both')

bg_color = '#077A7D'
tab_color = '#009999'

style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook', background=bg_color, borderwidth=0, tabposition='n')
style.configure('TNotebook.Tab', background=tab_color, foreground='#F5EEDD', padding=[10, 20], font=('Courier', 10))
style.map('TNotebook.Tab', background=[('selected', bg_color)])

click = 0
clickpers = 0
value = 10
value2 = 50
value3 = 1000
value4 = 100
mult = 2
clickpower = 1
plusclickpers = 1
krebirth = 0

root.title("Clicker")
root.geometry("700x550")
root.resizable(False, False)

def clicker():
    global click
    click += clickpower
    clickcount["text"] = f"{format_number(click)} clicks"
    widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"

def auto_click():
    global click
    if clickpers > 0:
        click += clickpers
        clickcount["text"] = f"{format_number(click)} clicks"
    root.after(1000, auto_click)

def show_notice(message):
    notice["text"] = message
    root.after(2000, lambda: notice.config(text=""))

def buy1():
    global click, clickpers, value, mult, plusclickpers
    if click >= value:
        click -= value
        clickpers += plusclickpers
        value *= mult
        clickcount["text"] = f"{format_number(click)} clicks"
        buy1["text"] = f"+{plusclickpers} click per second: {format_number(value)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        show_notice("Not enough clicks")

def buy2():
    global click, clickpower, value2, mult
    if click >= value2:
        click -= value2
        clickpower += 1
        value2 *= mult
        clickcount["text"] = f"{format_number(click)} clicks"
        buy2["text"] = f"+1 click power: {format_number(value2)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        show_notice("Not enough clicks")

def buy3():
    global click, clickpers, value3, mult
    if click >= value3:
        click -= value3
        clickpers *= 2
        value3 *= 2 * mult
        clickcount["text"] = f"{format_number(click)} clicks"
        buy3["text"] = f"double click per second: {format_number(value3)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        show_notice("Not enough clicks")

def buy4():
    global mult, krebirth
    if krebirth >= 2:
        mult /= 2
        krebirth -= 2
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        show_notice("Not enough rebirth")

def rebirth_func():
    global click, clickpers, clickpower, plusclickpers
    global value, value2, value3, value4, mult, krebirth
    if click >= value4:
        click = 0
        krebirth += 1
        clickpers = 0
        clickpower = 2 ** krebirth
        plusclickpers *= 2
        mult *= 2
        value = 10
        value2 = 50
        value3 = 1000
        value4 *= 10

        clickcount["text"] = f"{format_number(click)} clicks"
        buy1["text"] = f"+{plusclickpers} click per second: {format_number(value)}"
        buy2["text"] = f"+1 click power: {format_number(value2)}"
        buy3["text"] = f"double click per second: {format_number(value3)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
        rebirth["text"] = f"rebirth: {format_number(value4)}"
    else:
        show_notice("Not enough clicks")

reset_btn = tk.Button(tab2, text="Reset Game", command=reset_game,fg="#F5EEDD", bg="#8B0000", relief='sunken',activebackground="#8B0000", activeforeground="#F5EEDD")
reset_btn.place(anchor=tk.CENTER, x=350, y=360)

clickcount = Label(root, text=f"{format_number(click)} clicks", fg="#F5EEDD", bg='#077A7D')
clickcount.config(font=("Courier", 30))
clickcount.place(anchor=CENTER, x=350, y=120)

btn = Button(tab1, text="CLICK ME!", activeforeground="#F5EEDD", relief='sunken',activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=clicker)
btn.config(font=("Courier", 30))
btn.place(anchor=CENTER, x=350, y=150)

notice = Label(root, text="", fg="yellow", bg="#077A7D", font=("Courier", 12))
notice.place(anchor=CENTER, x=350, y=450)

buy1 = Button(tab2, text=f"+{plusclickpers} click per second: {format_number(value)}", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy1)
buy1.place(anchor=CENTER, x=350, y=210)

buy2 = Button(tab2, text=f"+1 click power: {format_number(value2)}", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy2)
buy2.place(anchor=CENTER, x=350, y=240)

buy3 = Button(tab2, text=f"double click per second: {format_number(value3)}", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy3)
buy3.place(anchor=CENTER, x=350, y=270)

buy4 = Button(tab2, text=f"divide value multiple: 2 rebirth", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy4)
buy4.place(anchor=CENTER, x=350, y=300)

rebirth = Button(tab1, text=f"rebirth: {format_number(value4)}", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=rebirth_func)
rebirth.place(anchor=CENTER, x=350, y=450)

widget = Label(tab1, text=f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}",fg="#F5EEDD", bg='#077A7D')
widget.config(font=("Courier", 12))
widget.place(anchor=CENTER, x=350, y=230)

load_progress()
auto_click()
auto_save()
root.mainloop()