from tkinter import *
import time
import humanize

root = Tk()
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
root.geometry("700x500")
root.resizable(False, False)
root["bg"] = "#077A7D"


def clicker():
    global click
    global clickpers
    global clickpower
    click += clickpower
    btn["text"] = humanize.intword(click)
    widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"


def auto_click():
    global click
    global clickpers
    if clickpers > 0:
        click += clickpers
        btn["text"] = humanize.intword(click)
    root.after(1000, auto_click)


def buy1():
    global click
    global clickpers
    global value
    global mult
    global plusclickpers
    if click >= value:
        click -= value
        clickpers += plusclickpers
        btn["text"] = humanize.intword(click)
        value *= mult
        buy1["text"] = f"+{plusclickpers} click per second: { humanize.intword(value)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        print("Not enough clicks")


def buy2():
    global click
    global clickpower
    global value2
    global mult
    if click >= value2:
        click -= value2
        clickpower += 1
        btn["text"] = humanize.intword(click)
        value2 *= mult
        buy2["text"] = f"+1 click power {humanize.intword(value2)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        print("Not enough clicks")


def buy3():
    global click
    global clickpers
    global value3
    global mult
    if click >= value3:
        click -= value3
        clickpers *= 2
        btn["text"] = humanize.intword(click)
        value3 *= 2 * mult
        buy3["text"] = f"double click per second: {humanize.intword(value3)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        print("Not enough clicks")


def buy4():
    global mult
    global krebirth
    if krebirth >= 2:
        mult /= 2
        krebirth -= 2
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
    else:
        print("Not enough rebirths")


def rebirth():
    global click
    global clickpers
    global clickpower
    global plusclickpers
    global value
    global value2
    global value3
    global value4
    global mult
    global krebirth
    if click >= value4:
        click = 0
        krebirth += 1
        clickpers = 0
        clickpower = 2**krebirth
        plusclickpers *= 2
        mult *= 2
        value = 10
        value2 = 50
        value3 = 1000
        value4 *= 10

        btn["text"] = humanize.intword(click)
        buy1["text"] = f"+{plusclickpers} click per second: { humanize.intword(value)}"
        buy2["text"] = f"+1 click power: {humanize.intword(value2)}"
        buy3["text"] = f"double click per second: {humanize.intword(value3)}"
        widget["text"] = f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}"
        rebirth["text"] = f"rebirth: {humanize.intword(value4)}"
    else:
        print("Not enough clicks")


btn = Button(root,text=humanize.intword(click),activeforeground="#F5EEDD",relief='sunken',activebackground="#06202B",fg="#F5EEDD",bg='#06202B',command=clicker)
btn.config(font=("Courier", 30))
btn.place(anchor=CENTER, x=350, y=150)
buy1 = Button(root,text=f"+{plusclickpers} click per second: { humanize.intword(value)}",activeforeground="#F5EEDD",relief='sunken',activebackground="#06202B",fg="#F5EEDD",bg='#06202B',command=buy1)
buy1.place(anchor=CENTER, x=350, y=210)
buy2 = Button(root,text=f"+1 click power: {humanize.intword(value2)}",activeforeground="#F5EEDD",relief='sunken',activebackground="#06202B",fg="#F5EEDD",bg='#06202B',command=buy2)
buy2.place(anchor=CENTER, x=350, y=240)
buy3 = Button(root,text=f"double click per second: {humanize.intword(value3)}",activeforeground="#F5EEDD",relief='sunken',activebackground="#06202B",fg="#F5EEDD",bg='#06202B',command=buy3)
buy3.place(anchor=CENTER, x=350, y=270)
buy4 = Button(root,text=f"divide value multiple: 2 rebirth",activeforeground="#F5EEDD",relief='sunken',activebackground="#06202B",fg="#F5EEDD",bg='#06202B',command=buy4)
buy4.place(anchor=CENTER, x=350, y=300)
rebirth = Button(root,text=f"rebirth: {humanize.intword(value4)}",activeforeground="#F5EEDD",relief='sunken',activebackground="#06202B",fg="#F5EEDD",bg='#06202B',command=rebirth)
rebirth.place(anchor=CENTER, x=350, y=470)
widget = Label(root,text=f"click per second: {clickpers}\n click power: {clickpower}\n rebirth: {krebirth}",fg="#F5EEDD",bg='#077A7D')
widget.place(anchor=CENTER, x=350, y=420)

auto_click()
root.mainloop()