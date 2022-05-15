from tkinter import *

def b1action():
   num1 = int(t1.get(1.0, END))
   num2 = int(t2.get(1.0, END))
   res = num1 + num2
   messagebox.showinfo("sum", res)
   
def b2action():
    num1 = int(t1.get(1.0, END))
    num2 = int(t2.get(1.0, END))
    res = num1 - num2
    t3.insert(1.0, res)

win = Tk()

win.title("My Calculator")

win.geometry("600x600")

l1 = Label(win, text="Enter a number:",font=('Arial',16) )
l1.grid(row=0, column=0, padx=5, pady=5)

t1 = Text(win, width=10, height=1, font=('Arial',13))
t1.grid(row=0, column=1, padx=5, pady=5)

l2 = Label(win, text="Enter a number:", font=('Arial', 16))
l2.grid(row=1, column=0, padx=5, pady=5)

t2 = Text(win, width=10, height=1, font=('Arial',13))
t2.grid(row=1, column=1, padx=5, pady=5)

b1 = Button(win, text="+", font=('Arial', 16), command=b1action)
b1.grid(row=2, column=0, padx=5, pady=5)

b2 = Button(win, text="-", font=('Arial', 16), command=b2action)
b2.grid(row=2, column=1, padx=5, pady=5)

l3 = Label(win, text="Result:",font=('Arial',16))
l3.grid(row=1, column=2)

t3 = Text(win, width=10, height=1, font=('Arial',13))
t3.grid(row=1, column=3)
win.mainloop()
    
    
    

