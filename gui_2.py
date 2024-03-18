# import tkinter as tk
# main_window = tk.Tk()
# lables
# Label(main_window)
# main_window.mainloop()

from tkinter import * 
main_window = Tk()


# Label
# Label(main_window,text="hello peeps").pack()
# Label(main_window,text="good morning").pack()

naem = Label(main_window,text="enter your name").grid(row=0,column=0)
age  = Label(main_window,text="enter your age").grid(row=1,column=0)


# Text
Entry(main_window,width=50,borderwidth=5).grid(row=0,column=1)
Entry(main_window,width=50,borderwidth=5).grid(row=1,column=1)


def done():
    print(f"my name is {naem.__getattribute__},and my age is {age.__getattribute__}")


# Button
Button(main_window,text= "done",command=done).grid(row=2,column=1)





main_window.mainloop()