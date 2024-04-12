from tkinter import Tk, Frame, Button, Label,Entry,Toplevel
from tkinter.ttk import Combobox
import math

window = Tk()
window.title('Calci Hub')
window.state('zoomed')

heading = Label(window, text="Calci Hub", font=('Forte', 50))
heading.place_configure(x=700,y=20)

sideBar = Frame(window, background="gray", width=window.winfo_width() - 1300, height=window.winfo_height(), borderwidth=5)
sideBar.place_configure(x=10,y=150)

def simple_calci():
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


    def appendValue(value):
        
        global exp, ExpressionDisplay
        
        if(value == ""):
            exp = ""
        else:
            exp += value
        ExpressionDisplay.place_forget()
        ExpressionDisplay = Label(SC, text=exp, font=("Aerial", FONT_SIZE+15))
        ExpressionDisplay.place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH - (FONT_SIZE/55*len(exp))*len(exp) , y=0.13*SCREEN_HEIGHT)

    def evaluate():
        prevIndexCarryForward = 0
        global exp,ExpressionDisplay
        for i in range(0, len(exp)):
            try:
                if exp[i] == "X":
                    operand1 = float(exp[prevIndexCarryForward:i-1])
                    operand2 = float(exp[i+2: len(exp)])
                    result = operand1 * operand2
                    exp = str(result)
                    break

                elif exp[i] == "/":
                    operand1 = float(exp[prevIndexCarryForward:i-1])
                    operand2 = float(exp[i+2: len(exp)])
                    result = operand1 / operand2
                    exp = str(result)
                    break

                elif exp[i] == "+":
                    operand1 = float(exp[prevIndexCarryForward:i-1])
                    operand2 = float(exp[i+2: len(exp)])
                    result = operand1 + operand2
                    exp = str(result)
                    break

                elif exp[i] == "-":
                    operand1 = float(exp[prevIndexCarryForward:i-1])
                    operand2 = float(exp[i+2: len(exp)])
                    result = operand1 - operand2
                    exp = str(result)
                    break
                
            except:
                exp = "Syntax Error"

            finally:
                ExpressionDisplay.place_forget()
                ExpressionDisplay = Label(SC, text=exp, font=("Aerial", FONT_SIZE+15))
                ExpressionDisplay.place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH - (FONT_SIZE/55*len(exp))*len(exp) , y=0.13*SCREEN_HEIGHT)

    L = Label(SC, text="Welcome to the calculator App !!!", font=("Aerial", FONT_SIZE, "bold"), width=30)
    L.place_configure(x=SCREEN_WIDTH//2 - 0.175*SCREEN_WIDTH , y=0.01*SCREEN_HEIGHT)

    exp = "harsh"

    ExpressionDisplay = Label(SC, text=exp, font=("Aerial", FONT_SIZE+15))
    ExpressionDisplay.place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH , y=0.13*SCREEN_HEIGHT)

    # row = 0
    startX = (INITIAL_PADDING_X + SCREEN_WIDTH - 4*BTN_WIDTH - SPACING_X)//4
    startY = (INITIAL_PADDING_Y + SCREEN_HEIGHT - 4*FONT_SIZE - SPACING_Y)//4

    Cancel = Button(SC, text="C", font=("Aerial", FONT_SIZE), fg="red", width=BTN_WIDTH, command=lambda: appendValue(""))
    Cancel.place_configure(x=startX, y=startY)

    Brackets = Button(SC, text="()", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("()"))
    Brackets.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY)

    Modulo = Button(SC, text="%", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" % "))
    Modulo.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY)

    Divide = Button(SC, text="/", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" / "))
    Divide.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY)

    # #row = 1
    nine = Button(SC, text="9", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("9"))
    nine.place_configure(x=startX, y=startY + FONT_SIZE + SPACING_Y)

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
    plusMinus = Button(SC, text="+/-", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("-+"))
    plusMinus.place_configure(x=startX, y=startY + 4*(FONT_SIZE + SPACING_Y))

    Zero = Button(SC, text="0", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("0"))
    Zero.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 4*(FONT_SIZE + SPACING_Y))

    Point = Button(SC, text=".", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("."))
    Point.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 4*(FONT_SIZE + SPACING_Y))

    Equals = Button(SC, text="=", font=("Aerial", FONT_SIZE),bg="green",fg="white", width=BTN_WIDTH, command=evaluate)
    Equals.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 4*(FONT_SIZE + SPACING_Y))

    SC.mainloop()

def compound_interest():
    #((P*(1+r)^n)-P)


    CI = Toplevel()
    CI.title('Compound interest calculator')
    CI.geometry('1300x650+230+135')
    CI.config(background='black')

    def cal_CI():
        p = float(PE.get())
        r = float(RE.get())
        t = float(TE.get())

        ans = p*((1+r)**t)

        ANS = Label(CI, text=f'The compound interest of amount {p} for {t} years at {r}% rate of interest is {ans}',font=('Aeiral', 20))
        ANS.place_configure(x = 150, y=550)
        Cal.config(state='disabled')

    #Welcome message
    WC = Label(CI, text='Welcome to the Compound interest calculator ',font=('forte', 30))
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
    SI = Toplevel()
    SI.title("Simple Interest calculator ")
    SI.geometry("1300x650+230+135")
    SI.config(background="black")

    def cal_SI():
        p = float(PE.get())
        r = float(RE.get())
        t = float(TE.get())

        ans = (p*r*t)/100

        ANS = Label(SI, text=f'The simple interest of amount {p} for {t} years at {r}% rate of interest is {ans}',font=('Aeiral', 20))
        ANS.place_configure(x = 150, y=550)
        Cal.config(state='disabled')

    #Welcome message
    WC = Label(SI, text='Welcome to the Simple interest calculator !!!',font=('forte', 30))
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
    Area = Toplevel()
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

def E_bill_calci():
    bill = Toplevel()
    bill.geometry('1300x650+230+135')
    bill.title('Electricity bill calculator')
    bill.configure(background='black')

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

    WC = Label(bill, text='Welcome to the Electricity bill calculator !!!',font=('forte', 30))
    WC.place_configure(x=250,y = 20)

    UL = Label(bill, text='Enter the units used in the month : ', font=('Verdana',25))
    UL.place_configure(x = 150, y=120)

    global UE
    UE = Entry(bill,font=('Verdana',25),width=15)
    UE.place_configure(x=850 ,y=120)

    Submit = Button(bill, text='SUBMIT' , font=('Verdana',23),command=calcu)
    Submit.place_configure(x=650, y=230)

    bill.mainloop()

B1 = Button(sideBar, text="simple calc", font=('Calibri', 20), borderwidth=10,width=13,command=simple_calci )
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="Compound interest ", font=('Calibri', 20), borderwidth=10,width=13 ,command=compound_interest)
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="Fixed deposit", font=('Calibri', 20), borderwidth=10,width=13,command=fixed_deposit )
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="Area Calculator", font=('Calibri', 20), borderwidth=10,width=13,command=Area_calci)
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="E Bill calculator", font=('Calibri', 20), borderwidth=10,width=13,command=E_bill_calci )
B1.pack(pady=20,padx=10)


window.mainloop()