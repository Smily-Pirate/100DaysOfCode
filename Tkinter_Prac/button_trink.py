from tkinter import ttk
from  tkinter import *
import tkinter as tk

window = Tk()

window.title('Multiple selection')

yscrollbar = Scrollbar(window)
yscrollbar.pack(side = RIGHT, fill = Y)

label = Label(window, text = "Select the languages below : ",
              font = ("Times New Roman", 10),
              padx = 10, pady = 10)

label.pack()
list = Listbox(window, selectmode = "multiple", yscrollcommand = yscrollbar.set)


list.pack(padx = 10, pady = 10, expand = YES, fill = "both")

x =["C", "C++", "C#", "Java", "Python",
    "R", "Go", "Ruby", "JavaScript", "Swift",
    "SQL", "Perl", "XML"]

for each_item in range(len(x)):

    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg = "lime")


yscrollbar.config(command = list.yview)
window.mainloop()

"""
window.geometry('200x250')

list = Listbox(window, selectmode = "multiple")

list.pack(expand = YES, fill = "both")

x = ["C", "C++", "Java", "Python"]

for each_item in range(len(x)):
    list.insert(END, x[each_item])

    list.itemconfig(each_item, bg = "yellow" if each_item % 2 == 0 else "cyan")

window.mainloop()

# root = tk.Tk()


# Creating a Tab with tkinter
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ='both')

ttk.Label(tab1, text="HERE \ YYYYY").grid(column = 100, row =0, padx = 30, pady = 30)
ttk.Label(tab2, text="Watashi \ YYYYY").grid(column = 0, row =100, padx = 30, pady = 30)

root.mainloop()

# Creating a button with Tkinter
root.geometry('100x100')

btn = Button(root, text = 'Click me !', command = root.destroy)

btn.pack(side = 'top')
root.mainloop()
"""