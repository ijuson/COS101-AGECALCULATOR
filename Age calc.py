from tkinter import *
from datetime import date

def calculateAge():
    today = date.today()
    birth_Date = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birth_Date.year - ((today.month, today.day) < (birth_Date.month, birth_Date.day))
    Label(text=f"{nameValue.get()} you are {age}years old", font=30).place(x=300, y=500)
