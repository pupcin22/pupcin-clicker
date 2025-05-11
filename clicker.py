from tkinter import *
import time
from tkinter import ttk
import tkinter as tk
import json
import random
SAVE_FILE = "clicker_save.json"

# Форматування чисел
def format_number(n):
    suffixes = [
        (10**100, 'G'), (10**63, 'Vg'), (10**60, 'Nd'), (10**57, 'Od'),
        (10**54, 'Sd'), (10**51, 'Sxd'), (10**48, 'Qd'), (10**45, 'Qtd'),
        (10**42, 'Td'), (10**39, 'Dd'), (10**36, 'Ud'), (10**33, 'Dc'),
        (10**30, 'No'), (10**27, 'Oc'), (10**24, 'Sp'), (10**21, 'Sx'),
        (10**18, 'Qi'), (10**15, 'Qa'), (10**12, 'T'), (10**9, 'B'),
        (10**6, 'M'), (10**3, 'K')
    ]
    for value, suffix in suffixes:
        if n >= value:
            return f"{n / value:.2f}{suffix}"
    return str(n)

# Глобальні змінні
click = 0
clickpers = 0
clickpower = 1
plusclickpers = 1
krebirth = 0
mult = 2
num1 = 0 
num2 = 0
num3 = 0
casinoval =10
# Ціни
value = 10
value2 = 50
value3 = 1000
value4 = 100
value5 = 50
value6 = 100
value7 = 50000

# Бонуси
bonus_clickpers_1 = 1
bonus_clickpower = 1
bonus_clickpers_10 = 10
bonus_clickpers_50 = 50
bonus_clickpers_100 = 100

# Збереження
def save_progress():
    data = {
        "click": click, "clickpers": clickpers, "clickpower": clickpower,
        "value": value, "value2": value2, "value3": value3, "value4": value4,
        "value5": value5, "value6": value6, "value7": value7,
        "mult": mult, "plusclickpers": plusclickpers, "krebirth": krebirth,
        "bonus_clickpers_1": bonus_clickpers_1,
        "bonus_clickpower": bonus_clickpower,
        "bonus_clickpers_10": bonus_clickpers_10,
        "bonus_clickpers_50": bonus_clickpers_50,
        "bonus_clickpers_100": bonus_clickpers_100,
        "casinoval":casinoval
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

# Завантаження
def load_progress():
    global click, clickpers, clickpower, value, value2, value3, value4,casinoval
    global value5, value6, value7, mult, plusclickpers, krebirth
    global bonus_clickpers_1, bonus_clickpower, bonus_clickpers_10, bonus_clickpers_50, bonus_clickpers_100
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
            value5 = data.get("value5", 50)
            value6 = data.get("value6", 100)
            value7 = data.get("value7", 5000)
            mult = data.get("mult", 2)
            plusclickpers = data.get("plusclickpers", 1)
            krebirth = data.get("krebirth", 0)
            bonus_clickpers_1 = data.get("bonus_clickpers_1", 1)
            bonus_clickpower = data.get("bonus_clickpower", 1)
            bonus_clickpers_10 = data.get("bonus_clickpers_10", 10)
            bonus_clickpers_50 = data.get("bonus_clickpers_50", 50)
            bonus_clickpers_100 = data.get("bonus_clickpers_100", 100)
            casinoval=data.get("casinoval",10)
    except FileNotFoundError:
        pass

def on_closing():
    save_progress()
    root.destroy()

# Скидання
def reset_game():
    global click, clickpers, clickpower, value, value2, value3, value4,casinoval
    global value5, value6, value7, mult, plusclickpers, krebirth
    global bonus_clickpers_1, bonus_clickpower, bonus_clickpers_10, bonus_clickpers_50, bonus_clickpers_100
    click = 0
    clickpers = 0
    clickpower = 1
    plusclickpers = 1
    krebirth = 0
    mult = 2
    value = 10
    value2 = 50
    value3 = 1000
    value4 = 100
    value5 = 50
    value6 = 100
    value7 = 5000
    casinoval =10
    bonus_clickpers_1 = 1
    bonus_clickpower = 1
    bonus_clickpers_10 = 10
    bonus_clickpers_50 = 50
    bonus_clickpers_100 = 100
    save_progress()
    update_texts()
    show_notice("Game reset!")

# Ігрові функції
def clicker():
    global click
    click += clickpower
    update_texts()

def auto_click():
    global click
    click += clickpers
    update_texts()
    root.after(1000, auto_click)

def show_notice(message):
    notice["text"] = message
    root.after(2000, lambda: notice.config(text=""))

def update_texts():
    clickcount["text"] = f"{format_number(click)} clicks"
    buy1_btn["text"] = f"+{bonus_clickpers_1} CPS: {format_number(value)}"
    buy2_btn["text"] = f"+{bonus_clickpower} click power: {format_number(value2)}"
    buy3_btn["text"] = f"Double CPS: {format_number(value3)}"
    rebirth["text"] = f"Rebirth: {format_number(value4)}"
    buy4_btn["text"] = f"+{bonus_clickpers_10} CPS: {format_number(value5)}"
    buy5_btn["text"] = f"+{bonus_clickpers_50} CPS: {format_number(value6)}"
    buy6_btn["text"] = f"+{bonus_clickpers_100} CPS: {format_number(value7)}"
    widget["text"] = f"CPS: {format_number(clickpers)}\nClick Power: {clickpower}\nRebirths: {krebirth}"
    casino_btn["text"]=f"Spin: {format_number(casinoval)} clicks"
    cas1["text"]=f"{num1}"
    cas2["text"]=f"{num2}"
    cas3["text"]=f"{num3}"
    

def buy1():
    global click, clickpers, value, bonus_clickpers_1
    if click >= value:
        click -= value
        clickpers += bonus_clickpers_1
        value *= mult
        bonus_clickpers_1 += 1
        update_texts()
    else:
        show_notice("Not enough clicks")

def buy2():
    global click, clickpower, value2, bonus_clickpower
    if click >= value2:
        click -= value2
        clickpower += bonus_clickpower
        value2 *= mult
        bonus_clickpower += 1
        update_texts()
    else:
        show_notice("Not enough clicks")

def buy3():
    global click, clickpers, value3
    if click >= value3:
        click -= value3
        clickpers *= 2
        value3 *= mult * 2
        update_texts()
    else:
        show_notice("Not enough clicks")

def buy4():
    global click, clickpers, value5, bonus_clickpers_10
    if click >= value5:
        click -= value5
        clickpers += bonus_clickpers_10
        value5 *= mult
        bonus_clickpers_10 += 10
        update_texts()
    else:
        show_notice("Not enough clicks")

def buy5():
    global click, clickpers, value6, bonus_clickpers_50
    if click >= value6:
        click -= value6
        clickpers += bonus_clickpers_50
        value6 *= mult
        bonus_clickpers_50 += 50
        update_texts()
    else:
        show_notice("Not enough clicks")

def buy6():
    global click, clickpers, value7, bonus_clickpers_100
    if click >= value7:
        click -= value7
        clickpers += bonus_clickpers_100
        value7 *= mult
        bonus_clickpers_100 += 100
        update_texts()
    else:
        show_notice("Not enough clicks")

def rebirth_func():
    global click, clickpers, clickpower, plusclickpers, value, value2, value3, value4,value5,value6,value7,casinoval, mult, krebirth,bonus_clickpers_1,bonus_clickpers_10,bonus_clickpers_50,bonus_clickpers_100
    if click >= value4:
        click = 0
        clickpers = 0
        bonus_clickpers_1 =1
        bonus_clickpers_10 =10
        bonus_clickpers_50 =50
        bonus_clickpers_100 =100
        clickpower = 2 ** (krebirth + 1)
        krebirth += 1
        plusclickpers *= 2
        mult *= 2
        value = 10
        value2 = 50
        value3 = 1000
        value4 *= 10
        value5 = 50
        value6 =100
        value7 =5000
        casinoval*=10
        update_texts()
    else:
        show_notice("Not enough clicks")
def casino():
    global num1,num2,num3,casinoval,click
    if click>=casinoval:
        click-=casinoval
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        if num1==num2 and num1==num3:
            click+=int(num2*casinoval*2)
            casinowin["text"]=f"YOU WIN JACKPOT{format_number(int(num2*casinoval*2))}"
        elif num1==num2 or num1 ==num3:
            click+=int(num1*casinoval*0.7)
            casinowin["text"]=f"YOU WIN {format_number(int(num1*casinoval*0.7))}"
        elif num2 == num3:
            click+=int(num2*casinoval*0.7)
            casinowin["text"]=f"YOU WIN {format_number(int(num2*casinoval*0.7))}"
        casinowin.after(3000, lambda: casinowin.config(text=""))
        update_texts()
    else:
        casinowin["text"]="Not enough clicks"

root = Tk()
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook, bg='#077A7D')
tab2 = tk.Frame(notebook, bg='#077A7D')
tab3 = tk.Frame(notebook, bg='#077A7D')
notebook.add(tab1, text='Clicker')
notebook.add(tab2, text='Upgrades')
notebook.add(tab3, text='Casino')
notebook.pack(expand=True, fill='both')

root.title("Clicker Game")
root.geometry("700x550")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook', background='#077A7D', borderwidth=0, tabposition='n')
style.configure('TNotebook.Tab', background='#009999', foreground='#F5EEDD', padding=[10, 20], font=('Courier', 10))
style.map('TNotebook.Tab', background=[('selected', '#077A7D')])

clickcount = Label(root, text=f"{format_number(click)} clicks", fg="#F5EEDD", bg='#077A7D')
clickcount.config(font=("Courier", 30))
clickcount.place(anchor=CENTER, x=350, y=120)

btn = Button(tab1, text="CLICK ME!", activeforeground="#F5EEDD", relief='sunken',activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=clicker)
btn.config(font=("Courier", 30))
btn.place(anchor=CENTER, x=350, y=150)

notice = Label(tab2, text="", fg="yellow", bg="#077A7D", font=("Courier", 12))
notice.place(anchor=CENTER, x=350, y=170)

buy1_btn = Button(tab2, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy1)
buy1_btn.place(anchor=CENTER, x=350, y=210)

buy2_btn = Button(tab2, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy2)
buy2_btn.place(anchor=CENTER, x=350, y=240)

buy3_btn = Button(tab2, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy3)
buy3_btn.place(anchor=CENTER, x=350, y=270)

buy4_btn = Button(tab2, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy4)
buy4_btn.place(anchor=CENTER, x=350, y=300)

buy5_btn = Button(tab2, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy5)
buy5_btn.place(anchor=CENTER, x=350, y=330)

buy6_btn = Button(tab2, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=buy6)
buy6_btn.place(anchor=CENTER, x=350, y=360)

cas1=Label(tab3, text="", fg="#F5EEDD", bg='#077A7D')
cas1.config(font=("Courier", 40))
cas1.place(anchor=CENTER, x=250, y=200)

cas2=Label(tab3, text="", fg="#F5EEDD", bg='#077A7D')
cas2.config(font=("Courier", 40))
cas2.place(anchor=CENTER, x=350, y=200)

cas3=Label(tab3, text="", fg="#F5EEDD", bg='#077A7D')
cas3.config(font=("Courier", 40))
cas3.place(anchor=CENTER, x=450, y=200)

casino_btn = Button(tab3, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=casino)
casino_btn.place(anchor=CENTER, x=350, y=360)

casinowin=Label(tab3, text="", fg="#F5EEDD", bg='#077A7D')
casinowin.config(font=("Courier", 20))
casinowin.place(anchor=CENTER, x=350, y=300)

rebirth = Button(tab1, text="", activeforeground="#F5EEDD",relief='sunken', activebackground="#06202B", fg="#F5EEDD", bg='#06202B', command=rebirth_func)
rebirth.place(anchor=CENTER, x=350, y=450)

widget = Label(tab1, text="", fg="#F5EEDD", bg='#077A7D')
widget.config(font=("Courier", 12))
widget.place(anchor=CENTER, x=350, y=230)


reset_btn = tk.Button(tab2, text="Reset Game", command=reset_game,fg="#F5EEDD", bg="#8B0000", relief='sunken',activebackground="#8B0000", activeforeground="#F5EEDD")
reset_btn.place(anchor=tk.CENTER, x=350, y=480)

load_progress()
update_texts()
auto_click()
root.after(1000, save_progress)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()