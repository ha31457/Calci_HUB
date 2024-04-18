from tkinter import Tk, Frame, Button, Label,Entry,Toplevel
from tkinter.ttk import Combobox
import math

window = Tk()
window.title('Calci Hub')
window.state('zoomed')
window.iconbitmap('calci.ico')

ACTIVE = []

def mouse_hover(widget, color="#FFFFFF"):
    widget.config(background=color)
def mouse_out(widget, color="#DDDDDD"):
    widget.config(background=color)


def simple_calci():
    for window in ACTIVE:
        window.withdraw()
    ACTIVE.clear()

    SCREEN_WIDTH = 1300
    BTN_WIDTH = 5
    SPACING_X = 111
    INITIAL_PADDING_X = SCREEN_WIDTH // 2 + 0.05 * SCREEN_WIDTH

    SCREEN_HEIGHT = 650
    FONT_SIZE = 20
    SPACING_Y = 65
    INITIAL_PADDING_Y = SCREEN_HEIGHT // 2 + 0.001 * SCREEN_HEIGHT


    SC =Toplevel()
    SC.title("Calculator App !!!")
    SC.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+230+125")
    SC.configure(bg="black")

    ACTIVE.append(SC)

    def appendValue(value):
        if(value == ""):
            expressionHandle[0] = ""
        else:
            expressionHandle[0] += value
        expressionHandle[1].place_forget()
        expressionHandle[1] = Label(SC, text=expressionHandle[0], font=("Aerial", FONT_SIZE+15))
        expressionHandle[1].place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH - (FONT_SIZE/55*len(expressionHandle[0]))*len(expressionHandle[0]) , y=0.13*SCREEN_HEIGHT)

    def delete():
        expressionHandle[0] = expressionHandle[0][0 : len(expressionHandle[0])-1]
        expressionHandle[1].place_forget()
        expressionHandle[1] = Label(SC, text=expressionHandle[0], font=("Aerial", FONT_SIZE+15))
        expressionHandle[1].place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH - (FONT_SIZE/55*len(expressionHandle[0]))*len(expressionHandle[0]) , y=0.13*SCREEN_HEIGHT)

    def evaluate():
        prevIndexCarryForward = 0
        exp = expressionHandle[0]
        try:
            if("SQRT" in expressionHandle[0]):
                try:
                    operand = float(expressionHandle[0][5:len(expressionHandle[0])])
                except:
                    try:
                        operand = float(expressionHandle[0][0:expressionHandle[0].index("S")])
                    except:
                        print("error")
                result = math.sqrt(operand)
                expressionHandle[0] = str(result)

            else:
                for i in range(0, len(expressionHandle[0])):
                    if expressionHandle[0][i] == "X":
                        operand1 = float(expressionHandle[0][prevIndexCarryForward:i-1])
                        operand2 = float(expressionHandle[0][i+2: len(expressionHandle[0])])
                        result = operand1 * operand2
                        expressionHandle[0] = str(result)
                        break

                    elif expressionHandle[0][i] == "/":
                        operand1 = float(expressionHandle[0][prevIndexCarryForward:i-1])
                        operand2 = float(expressionHandle[0][i+2: len(expressionHandle[0])])
                        result = operand1 / operand2
                        expressionHandle[0] = str(result)
                        break

                    elif expressionHandle[0][i] == "+":
                        operand1 = float(expressionHandle[0][prevIndexCarryForward:i-1])
                        operand2 = float(expressionHandle[0][i+2: len(expressionHandle[0])])
                        result = operand1 + operand2
                        expressionHandle[0] = str(result)
                        break

                    elif expressionHandle[0][i] == "-":
                        operand1 = float(expressionHandle[0][prevIndexCarryForward:i-1])
                        operand2 = float(expressionHandle[0][i+2: len(expressionHandle[0])])
                        result = operand1 - operand2
                        expressionHandle[0] = str(result)
                        break

                    elif expressionHandle[0][i] == "%":
                        operand1 = float(expressionHandle[0][prevIndexCarryForward:i-1])
                        operand2 = float(expressionHandle[0][i+2: len(expressionHandle[0])])
                        result = operand1 % operand2
                        expressionHandle[0] = str(result)
                        break

                
        except Exception as e:
            print(e)
            expressionHandle[0] = "Syntax Error"

        finally:
            expressionHandle[1].place_forget()
            expressionHandle[1] = Label(SC, text=expressionHandle[0], font=("Aerial", FONT_SIZE+15))
            expressionHandle[1].place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH - (FONT_SIZE/55*len(expressionHandle[0]))*len(expressionHandle[0]) , y=0.13*SCREEN_HEIGHT)
            value = f"{exp} = {expressionHandle[0]}"
            with open("history.txt", "a") as f:
                f.write(f'''
{value}''')
            
                Label(historyFrame, text=value, font=("Arial", FONT_SIZE-10)).pack()


    L = Label(SC, text="Welcome to the calculator App !!!", font=("Aerial", FONT_SIZE, "bold"), width=30)
    L.place_configure(x=SCREEN_WIDTH//2 - 0.175*SCREEN_WIDTH , y=0.01*SCREEN_HEIGHT)

    exp = "harsh"
    ExpressionDisplay = Label(SC, text=exp, font=("Aerial", FONT_SIZE+15))

    expressionHandle = [exp, ExpressionDisplay]
    expressionHandle[1].place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH , y=0.13*SCREEN_HEIGHT)

    with open("history.txt", "r") as f:
        historyList = f.readlines()

    # row = 0
    startX = (INITIAL_PADDING_X + SCREEN_WIDTH - 4*BTN_WIDTH - SPACING_X)//4
    startY = (INITIAL_PADDING_Y + SCREEN_HEIGHT - 4*FONT_SIZE - SPACING_Y)//4

    historyFrame = Frame(SC)
    historyFrame.place_configure(x=SPACING_X-32.9, y=startY)

    historyFrame.bind("<Enter>", lambda e: mouse_hover(historyFrame, color="#FEFEFE"))
    historyFrame.bind("<Leave>", lambda e: mouse_out(historyFrame, color="#EEEEEE"))

    Label(historyFrame, text="HISTORY", font=("Arial", FONT_SIZE+5, "bold")).pack()


    for i in range(len(historyList)):
        value = historyList[i]
        value = value[0:len(value)-1]
        Label(historyFrame, text=value, font=("Arial", FONT_SIZE-10)).pack()

    Cancel = Button(SC, text="C", font=("Aerial", FONT_SIZE), fg="red", width=BTN_WIDTH, command=lambda: appendValue(""))
    Cancel.place_configure(x=startX, y=startY)

    sqRoot = Button(SC, text="SQRT", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("SQRT "))
    sqRoot.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY)

    Modulo = Button(SC, text="%", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" % "))
    Modulo.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY)

    Divide = Button(SC, text="/", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" / "))
    Divide.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY)

    # #row = 1
    Nine = Button(SC, text="9", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("9"))
    Nine.place_configure(x=startX, y=startY + FONT_SIZE + SPACING_Y)

    Eight = Button(SC, text="8", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("8"))
    Eight.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + FONT_SIZE + SPACING_Y)

    Seven = Button(SC, text="7", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("7"))
    Seven.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + FONT_SIZE + SPACING_Y)

    Multiply = Button(SC, text="X", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" X "))
    Multiply.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + FONT_SIZE + SPACING_Y)

    # #row = 2
    Six = Button(SC, text="6", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("6"))
    Six.place_configure(x=startX, y=startY + 2*(FONT_SIZE + SPACING_Y))

    Five = Button(SC, text="5", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("5"))
    Five.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 2*(FONT_SIZE + SPACING_Y))

    Four = Button(SC, text="4", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("4"))
    Four.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 2*(FONT_SIZE + SPACING_Y))

    Subtract = Button(SC, text="-", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" - "))
    Subtract.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 2*(FONT_SIZE + SPACING_Y))

    # #row = 3
    Three = Button(SC, text="3", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("3"))
    Three.place_configure(x=startX, y=startY + 3*(FONT_SIZE + SPACING_Y))

    Two = Button(SC, text="2", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("2"))
    Two.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 3*(FONT_SIZE + SPACING_Y))

    One = Button(SC, text="1", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("1"))
    One.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 3*(FONT_SIZE + SPACING_Y))

    Add = Button(SC, text="+", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" + "))
    Add.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 3*(FONT_SIZE + SPACING_Y))

    # #row = 4
    Del = Button(SC, text="DEL", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=delete)
    Del.place_configure(x=startX, y=startY + 4*(FONT_SIZE + SPACING_Y))

    Zero = Button(SC, text="0", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("0"))
    Zero.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 4*(FONT_SIZE + SPACING_Y))

    Point = Button(SC, text=".", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("."))
    Point.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 4*(FONT_SIZE + SPACING_Y))

    Equals = Button(SC, text="=", font=("Aerial", FONT_SIZE),bg="green",fg="white", width=BTN_WIDTH, command=evaluate)
    Equals.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 4*(FONT_SIZE + SPACING_Y))


    Cancel.bind("<Enter>", lambda e: mouse_hover(Cancel))
    Cancel.bind("<Leave>", lambda e: mouse_out(Cancel))
    sqRoot.bind("<Enter>", lambda e: mouse_hover(sqRoot))
    sqRoot.bind("<Leave>", lambda e: mouse_out(sqRoot))
    Modulo.bind("<Enter>", lambda e: mouse_hover(Modulo))
    Modulo.bind("<Leave>", lambda e: mouse_out(Modulo))
    Divide.bind("<Enter>", lambda e: mouse_hover(Divide))
    Divide.bind("<Leave>", lambda e: mouse_out(Divide))
    Nine.bind("<Enter>", lambda e: mouse_hover(Nine))
    Nine.bind("<Leave>", lambda e: mouse_out(Nine))
    Eight.bind("<Enter>", lambda e: mouse_hover(Eight))
    Eight.bind("<Leave>", lambda e: mouse_out(Eight))
    Seven.bind("<Enter>", lambda e: mouse_hover(Seven))
    Seven.bind("<Leave>", lambda e: mouse_out(Seven))
    Multiply.bind("<Enter>", lambda e: mouse_hover(Multiply))
    Multiply.bind("<Leave>", lambda e: mouse_out(Multiply))
    Six.bind("<Enter>", lambda e: mouse_hover(Six))
    Six.bind("<Leave>", lambda e: mouse_out(Six))
    Five.bind("<Enter>", lambda e: mouse_hover(Five))
    Five.bind("<Leave>", lambda e: mouse_out(Five))
    Four.bind("<Enter>", lambda e: mouse_hover(Four))
    Four.bind("<Leave>", lambda e: mouse_out(Four))
    Subtract.bind("<Enter>", lambda e: mouse_hover(Subtract))
    Subtract.bind("<Leave>", lambda e: mouse_out(Subtract))
    Three.bind("<Enter>", lambda e: mouse_hover(Three))
    Three.bind("<Leave>", lambda e: mouse_out(Three))
    Two.bind("<Enter>", lambda e: mouse_hover(Two))
    Two.bind("<Leave>", lambda e: mouse_out(Two))
    One.bind("<Enter>", lambda e: mouse_hover(One))
    One.bind("<Leave>", lambda e: mouse_out(One))
    Add.bind("<Enter>", lambda e: mouse_hover(Add))
    Add.bind("<Leave>", lambda e: mouse_out(Add))
    Del.bind("<Enter>", lambda e: mouse_hover(Del))
    Del.bind("<Leave>", lambda e: mouse_out(Del))
    Zero.bind("<Enter>", lambda e: mouse_hover(Zero))
    Zero.bind("<Leave>", lambda e: mouse_out(Zero))
    Point.bind("<Enter>", lambda e: mouse_hover(Point))
    Point.bind("<Leave>", lambda e: mouse_out(Point))
    Equals.bind("<Enter>", lambda e: mouse_hover(Equals, "#00AA00"))
    Equals.bind("<Leave>", lambda e: mouse_out(Equals, "#009900"))


    SC.mainloop()

def compound_interest():
    
    for window in ACTIVE:
        window.withdraw()
    ACTIVE.clear()
    CI = Toplevel()
    CI.title('Compound interest calculator')
    CI.geometry('1300x650+230+135')
    CI.config(background='black')

    ACTIVE.append(CI)

    def cal_CI():
        p = float(PE.get())
        r = float(RE.get())
        t = float(TE.get())

        ans = p*((1+r)**t)

        ANS = Label(CI, text=f'The compound interest of amount {p} for {t} years at {r}% rate of interest is {ans}',font=('Aeiral', 20))
        ANS.place_configure(x = 150, y=550)
        Cal.config(state='disabled')

    #Welcome message
    WC = Label(CI, text='Welcome to the Compound interest calculator ',font=('Verdana', 30))
    WC.place_configure(x=250,y = 20)

    #Principal 
    PL = Label(CI, text="Enter the principal amount ",font=('Aerial', 20),width=25)
    PL.place_configure(x = 200, y = 120)
    PE = Entry(CI,font=('Aerial', 20))
    PE.place_configure(x=750, y=120)

    #rate
    RL = Label(CI, text='Enter the rate of interest : ',font=('Aerial', 20),width=25)
    RL.place_configure(x = 200, y = 220)
    RE = Entry(CI,font=('Aerial', 20))
    RE.place_configure(x = 750, y = 220)

    #Time 
    TL = Label(CI, text='Enter the time period : ',font=('Aerial', 20),width=25)
    TL.place_configure(x=200, y=320)
    TE = Entry(CI,font=('Aerial', 20))
    TE.place_configure(x = 750, y=320)

    #button
    Cal = Button(CI, text='CALCULATE !',font=('Aerial', 20),command=cal_CI)
    Cal.place_configure(x = 570, y = 420)


    CI.mainloop()

def fixed_deposit():
    for window in ACTIVE:
        window.withdraw()
    ACTIVE.clear()
    SI = Toplevel()
    SI.title("Fixed Deposit calculator ")
    SI.geometry("1300x650+230+135")
    SI.config(background="black")

    ACTIVE.append(SI)

    def cal_SI():
        p = float(PE.get())
        r = float(RE.get())
        t = float(TE.get())

        ans = (p*r*t)/100

        ANS = Label(SI, text=f'The interest of amount {p} for {t} years at {r}% rate of interest is {ans}',font=('Aeiral', 20))
        ANS.place_configure(x = 150, y=550)
        Cal.config(state='disabled')

    #Welcome message
    WC = Label(SI, text='Welcome to the fixed deposit calculator !!!',font=('Verdana', 30))
    WC.place_configure(x=250,y = 20)

    #Principal 
    PL = Label(SI, text="Enter the principal amount ",font=('Aerial', 20),width=25)
    PL.place_configure(x = 200, y = 120)
    PE = Entry(SI,font=('Aerial', 20))
    PE.place_configure(x=750, y=120)

    #rate
    RL = Label(SI, text='Enter the rate of interest : ',font=('Aerial', 20),width=25)
    RL.place_configure(x = 200, y = 220)
    RE = Entry(SI,font=('Aerial', 20))
    RE.place_configure(x = 750, y = 220)

    #Time 
    TL = Label(SI, text='Enter the time period : ',font=('Aerial', 20),width=25)
    TL.place_configure(x=200, y=320)
    TE = Entry(SI,font=('Aerial', 20))
    TE.place_configure(x = 750, y=320)

    #button
    Cal = Button(SI, text='CALCULATE !',font=('Aerial', 20),command=cal_SI)
    Cal.place_configure(x = 570, y = 420)

    SI.mainloop()

def Area_calci():

    for window in ACTIVE:
        window.withdraw()
    ACTIVE.clear()
    Area = Toplevel()
    Area.geometry('1300x650+230+135')
    Area.title('Area Calculator')
    Area.config(background='black')

    ACTIVE.append(Area)

    def display():
        
        Submit_1.destroy() #Submit1 was at x=600 and y=200
        Selector.config(state='disabled')

        v = Selector.get()
        if v == 'Circle':
            L1 = Label(Area , text='Please enter the radius of the circle : ',font=('Verdana',25))
            L1.place_configure(x=150, y=250)
            
            global R
            R = Entry(Area,font=('Verdana',25),width=10)
            R.place_configure(x = 1000, y=250)
            Submit = Button(Area, text='Submit',font=('Verdana',25),command=cir).place_configure(x=600, y=320)

        elif v == 'Square':
            L1 = Label(Area , text='Please enter the side of the square : ',font=('Verdana',25))
            L1.place_configure(x=150, y=250)
            global s
            s = Entry(Area,font=('Verdana',25),width=10)
            s.place_configure(x = 1000, y=250)
            Submit = Button(Area, text='Submit',font=('Verdana',25),command=sqr).place_configure(x=600, y=320)

        elif v == 'Rectangle':
            L1 = Label(Area, text='Enter the length of the rectangle :', font=('Verdana', 25))
            L1.place_configure(x=150, y=250)
            global l , w
            l = Entry(Area,font=('Verdana',25),width=10)
            l.place_configure(x = 1000, y=250)
            L2 = Label(Area, text='Enter the width of the rectangle : ',font=('Verdana', 25))
            L2.place_configure(x=150, y=350)
            w = Entry(Area,font=('Verdana', 25),width=10)
            w.place_configure(x = 1000, y=350)
            Submit = Button(Area, text='Submit',font=('Verdana',25),command=rec).place_configure(x=600, y=450)

        elif v == 'Triangle':
            L1 = Label(Area, text='Enter the base of the triangle :', font=('Verdana', 25))
            L1.place_configure(x=150, y=250)
            global b,h
            b = Entry(Area,font=('Verdana',25))
            b.place_configure(x = 1000, y=250)
            L2 = Label(Area, text='Enter the height of the triangle : ',font=('Verdana', 25))
            L2.place_configure(x=150, y=350)
            h = Entry(Area,font=('Verdana', 25))
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
            
    WC = Label(Area, text='Welcome to the Area calculator !!!',font=('Verdana', 30))
    WC.place_configure(x=330,y = 20)

    SEL = Label(Area, text='Select the shape of your choice to find area ',font=('Verdana',25))
    SEL.place_configure(x = 110, y=120)

    val = ['Select','Circle', 'Square', 'Rectangle', 'Triangle']
    Selector = Combobox(Area, values=val,font=('Verdana',18))
    Selector.current(0)
    Selector.place_configure(x=1020,y = 120,height=50,width=150)

    Submit_1 = Button(Area, text='Submit',font=('Verdana',25),command=display)
    Submit_1.place_configure(x = 600,y=200)


    Area.mainloop()

def E_bill_calci():

    for window in ACTIVE:
        window.withdraw()
    ACTIVE.clear()
    bill = Toplevel()
    bill.geometry('1300x650+230+135')
    bill.title('Electricity bill calculator')
    bill.configure(background='black')

    ACTIVE.append(bill)

    def calcu():
        UE.config(state='disabled')
        Submit.config(state='disabled')
        unit =int(UE.get())

        if unit <= 100:
            ans = unit*1.5
        elif unit <= 400:
            ans = 100*1.5 + (unit-100)*1.75
        elif unit <= 600:
            ans = 100*1.5 + 300*1.75 + (unit-400)*2
        else:
            ans = 100*1.5 + 300*1.75 + 300*2 + (unit-600)*2.5


        if ans > 50:
            ans += (ans*0.15)
        else:
            ans += 150

        ANS = Label(bill, text=f'The total bill with use of {unit} units is {ans}', font=('Verdana',25))
        ANS.place_configure(x=280,y=370)

    WC = Label(bill, text='Welcome to the Electricity bill calculator !!!',font=('Verdana', 30))
    WC.place_configure(x=250,y = 20)

    UL = Label(bill, text='Enter the units used in the month : ', font=('Verdana',25))
    UL.place_configure(x = 150, y=120)

    global UE
    UE = Entry(bill,font=('Verdana',25),width=15)
    UE.place_configure(x=850 ,y=120)

    Submit = Button(bill, text='SUBMIT' , font=('Verdana',23),command=calcu)
    Submit.place_configure(x=650, y=230)

    bill.mainloop()



title = Frame(window, background="gray", width=window.winfo_width() - 1300, height=window.winfo_height(), borderwidth=5)
# title.place_configure(x=0,y=0)
title.grid(row=0, column=0)

heading = Label(title, text="Calci Hub", font=('Forte', 50), background="gray")
heading.grid(row=0, column=1, padx=700)

sideBar = Frame(window, background="gray", width=window.winfo_width() - 1300, height=window.winfo_height(), borderwidth=5)
# sideBar.place_configure(x=10,y=150)
sideBar.grid(row=1,column=0, sticky="W", pady=15, padx=5)

B1 = Button(sideBar, text="Simple", font=('Calibri', 20), borderwidth=10,width=13,command=simple_calci, )
B1.pack(pady=20,padx=5)
B2 = Button(sideBar, text="Compound", font=('Calibri', 20), borderwidth=10,width=13 ,command=compound_interest, )
B2.pack(pady=20,padx=5)
B3 = Button(sideBar, text="Fixed Deposit", font=('Calibri', 20), borderwidth=10,width=13,command=fixed_deposit, )
B3.pack(pady=20,padx=5)
B4 = Button(sideBar, text="Area", font=('Calibri', 20), borderwidth=10,width=13,command=Area_calci, )
B4.pack(pady=20,padx=5)
B5 = Button(sideBar, text="E Bill", font=('Calibri', 20), borderwidth=10,width=13,command=E_bill_calci, )
B5.pack(pady=20,padx=5)

B1.bind("<Enter>", lambda e: mouse_hover(B1))
B1.bind("<Leave>", lambda e: mouse_out(B1))
B2.bind("<Enter>", lambda e: mouse_hover(B2))
B2.bind("<Leave>", lambda e: mouse_out(B2))
B3.bind("<Enter>", lambda e: mouse_hover(B3))
B3.bind("<Leave>", lambda e: mouse_out(B3))
B4.bind("<Enter>", lambda e: mouse_hover(B4))
B4.bind("<Leave>", lambda e: mouse_out(B4))
B5.bind("<Enter>", lambda e: mouse_hover(B5))
B5.bind("<Leave>", lambda e: mouse_out(B5))

root = Toplevel()
root.geometry('1300x650+230+135')
root.title('slider')

txt = "Welcome to Calci Hub. Your one stop solution for calculating !"
count = 0
text = ""

label = Label(root, text=txt, font=('Verdana',25,'bold'), fg='black')
label.pack(pady=300)

handler = [count, text]

def slider():
    if handler[0] >= len(txt):
        handler[0] = -1
        handler[1] = ''
        label.config(text=handler[1])

    else:
        handler[1] = handler[1] + txt[handler[0]]
        label.config(text=handler[1])
    handler[0] += 1

    label.after(150,slider)

slider()
root.mainloop()

window.mainloop()