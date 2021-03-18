import sqlite3
my_conn = sqlite3.connect('register.db')
import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("1300x250")
r_set=my_conn.execute('''SELECT * from Comp ''');
i=0 # row value inside the loop
for Comp in r_set:
for j in range(len(Comp)):
e = Entry(my_w, width=10, fg='black')
e.grid(row=i, column=j)
e.insert(END, Comp[j])
i=i+1
my_w.mainloop()