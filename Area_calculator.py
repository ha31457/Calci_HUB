from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Combobox
import math

Area = Tk()
Area.geometry('1300x650+230+135')
Area.title('Area Calculator')
Area.config(background='black')

def display():
    
    Submit_1.destroy() #Submit1 was at x=600 and y=200
    Selector.config(state='disabled')

    v = Selector.get()
    if v == 'Circle':
        L1 = Label(Area , text='Please enter the radius of the circle : ',font=('Verdana',25))
        L1.place_configure(x=150, y=250)
        
        global R
        R = Entry(font=('Verdana',25),width=10)
        R.place_configure(x = 1000, y=250)
        Submit = Button(Area, text='Submit',font=('Verdana',25),command=cir).place_configure(x=600, y=320)

    elif v == 'Square':
        L1 = Label(Area , text='Please enter the side of the square : ',font=('Verdana',25))
        L1.place_configure(x=150, y=250)
        global s
        s = Entry(font=('Verdana',25),width=10)
        s.place_configure(x = 1000, y=250)
        Submit = Button(Area, text='Submit',font=('Verdana',25),command=sqr).place_configure(x=600, y=320)

    elif v == 'Rectangle':
        L1 = Label(Area, text='Enter the length of the rectangle :', font=('Verdana', 25))
        L1.place_configure(x=150, y=250)
        global l , w
        l = Entry(font=('Verdana',25),width=10)
        l.place_configure(x = 1000, y=250)
        L2 = Label(Area, text='Enter the width of the rectangle : ',font=('Verdana', 25))
        L2.place_configure(x=150, y=350)
        w = Entry(font=('Verdana', 25),width=10)
        w.place_configure(x = 1000, y=350)
        Submit = Button(Area, text='Submit',font=('Verdana',25),command=rec).place_configure(x=600, y=450)

    elif v == 'Triangle':
        L1 = Label(Area, text='Enter the base of the triangle :', font=('Verdana', 25))
        L1.place_configure(x=150, y=250)
        global b,h
        b = Entry(font=('Verdana',25))
        b.place_configure(x = 1000, y=250)
        L2 = Label(Area, text='Enter the height of the triangle : ',font=('Verdana', 25))
        L2.place_configure(x=150, y=350)
        h = Entry(font=('Verdana', 25))
        h.place_configure(x = 1000, y=350)
        Submit = Button(Area, text='Submit',font=('Verdana',25),command=tri).place_configure(x=600, y=450)
    
    else:
       Ans = Label(Area, text='Please select a shape to find area ', font=('Verdana',25))
       Ans.place_configure(x=600, y=350) 
#       Selector.config(state='normal')
 #      Submit_1.place_configure(x = 600,y=200)

def cir():
    
    r = int(R.get())
    ans = math.pi*r*r
    Ans = Label(Area, text=f'The area of circle with radius {r} is {ans}', font=('Verdana',25))
    Ans.place_configure(x=200, y=450)

def sqr():
    S = int(s.get())
    ans = S*S
    Ans = Label(Area, text=f'The area of square with side {S} is {ans}', font=('Verdana',25))
    Ans.place_configure(x=200, y=450)

def rec():
    L = int(l.get())
    W = int(w.get())

    ans = L*W
    Ans = Label(Area, text=f'The area of rectangle with length {L} and width {W} is {ans}', font=('Verdana',25))
    Ans.place_configure(x=200, y=550)

def tri():
    B = int(b.get())
    H = int(h.get())
    ans = 0.5*B*H
    Ans = Label(Area, text=f'The area of triangle with base {B}and height {H} is {ans}', font=('Verdana',25))
    Ans.place_configure(x=200, y=550)
        
WC = Label(Area, text='Welcome to the Area calculator !!!',font=('forte', 30))
WC.place_configure(x=330,y = 20)

SEL = Label(Area, text='Select the shape of your choice to find area ',font=('Verdana',25))
SEL.place_configure(x = 110, y=120)

val = ['Select','Circle', 'Square', 'Rectangle', 'Triangle']
Selector = Combobox(Area, values=val)
Selector.current(0)
Selector.place_configure(x=1020,y = 120,height=50,width=150)

Submit_1 = Button(Area, text='Submit',font=('Verdana',25),command=display)
Submit_1.place_configure(x = 600,y=200)


Area.mainloop()
