from tkinter import *
from datetime import date

def calculateAge():
    today = date.today()
    birth_Date = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birth_Date.year - ((today.month, today.day) < (birth_Date.month, birth_Date.day))
    Label(text=f"{nameValue.get()} you are {age}years old", font=30).place(x=300, y=500)

window = Tk()
window.title("Age Calculator")
window.geometry("750x550")

Heading = Label(text="AGE CALCULATOR", font=("arial", 50, "bold"))
Label(text="NAME", font=23).place(x=140, y=250)
Label(text="YEAR", font=23).place(x=140, y=300)
Label(text="MONTH", font=23).place(x=140, y=350)
Label(text="DAY", font=23).place(x=140, y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(window, textvariable=nameValue, width=30, bd=3, font=20)
nameEntry.place(x=300, y=250)

yearEntry = Entry(window, textvariable=yearValue, width=30, bd=3, font=20)
yearEntry.place(x=300, y=300)

monthEntry = Entry(window, textvariable=monthValue, width=30, bd=3, font=20)
monthEntry.place(x=300, y=350)
