from tkinter import *
root = Tk() 
root.title("calculator")


# Text

e = Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=30)

# functions
list_of_number = []

def number_input(number):
    current_value= e.get()
    e.delete(0,END)
    e.insert(0,str(current_value)+str(number))

def clear_values():
    list_of_number.clear()
    e.delete(0,END)

def sum_of_values():
    num1=e.get()
    list_of_number.append(num1)
    e.delete(0,END)


# def sub_of_values():
#     num1=e.get()
#     list_of_number.append(num1)
#     e.delete(0,END)

def equals():
    num1=e.get()
    list_of_number.append(int(num1))
    e.delete(0,END)

    sum=0
    for values in list_of_number:
        sum+= int(values)
    e.insert(0,str(sum))

    # sub=0
    # for values in list_of_number:
    #     sub-=int(values)
    

     




# Button

but9= Button(root,text="9",padx=40,pady=20,command=lambda:number_input(9)).grid(row=1,column=0)
but8= Button(root,text="8",padx=40,pady=20,command=lambda:number_input(8)).grid(row=1,column=1)
but7= Button(root,text="7",padx=40,pady=20,command=lambda:number_input(7)).grid(row=1,column=2)

but6= Button(root,text="6",padx=40,pady=20,command=lambda:number_input(6)).grid(row=2,column=0)
but5= Button(root,text="5",padx=40,pady=20,command=lambda:number_input(5)).grid(row=2,column=1)
but4= Button(root,text="4",padx=40,pady=20,command=lambda:number_input(4)).grid(row=2,column=2)


but3= Button(root,text="3",padx=40,pady=20,command=lambda:number_input(3)).grid(row=3,column=0)
but2= Button(root,text="2",padx=40,pady=20,command=lambda:number_input(2)).grid(row=3,column=1)
but1= Button(root,text="1",padx=40,pady=20,command=lambda:number_input(1)).grid(row=3,column=2)




# but_sub= Button(root,text="-",padx=40,pady=20,command=sub_of_values()).grid(row=3,column=0)
but0= Button(root,text="0",padx=40,pady=20,command=number_input(0)).grid(row=4,column=1)
but_add= Button(root,text="+",padx=40,pady=20,command=sum_of_values).grid(row=4,column=2)


but_clear = Button(root,text="cls",padx=30,pady=30,command=clear_values).grid(row=4,column=0)
but_equals_to = Button(root,text="=",padx=30,pady=30,command=equals).grid(row=5,column=0)


root.mainloop()