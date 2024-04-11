
from tkinter import *

SCREEN_WIDTH = 1300
BTN_WIDTH = 5
SPACING_X = 111
INITIAL_PADDING_X = SCREEN_WIDTH // 2 + 0.05 * SCREEN_WIDTH

SCREEN_HEIGHT = 650
FONT_SIZE = 20
SPACING_Y = 65
INITIAL_PADDING_Y = SCREEN_HEIGHT // 2 + 0.001 * SCREEN_HEIGHT


w =Tk()
w.title("Calculator App !!!")
w.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+230+125")
w.configure(bg="black")


def appendValue(value):
    global exp, ExpressionDisplay
    if(value == ""):
        exp = ""
    else:
        exp += value
    ExpressionDisplay.place_forget()
    ExpressionDisplay = Label(w, text=exp, font=("Aerial", FONT_SIZE+15))
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
            ExpressionDisplay = Label(w, text=exp, font=("Aerial", FONT_SIZE+15))
            ExpressionDisplay.place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH - (FONT_SIZE/55*len(exp))*len(exp) , y=0.13*SCREEN_HEIGHT)

L = Label(w, text="Welcome to the calculator App !!!", font=("Aerial", FONT_SIZE, "bold"), width=30)
L.place_configure(x=SCREEN_WIDTH//2 - 0.175*SCREEN_WIDTH , y=0.01*SCREEN_HEIGHT)

exp = "harsh"

ExpressionDisplay = Label(w, text=exp, font=("Aerial", FONT_SIZE+15))
ExpressionDisplay.place_configure(x=SCREEN_WIDTH//2 - 0.03*SCREEN_WIDTH , y=0.13*SCREEN_HEIGHT)

# row = 0
startX = (INITIAL_PADDING_X + SCREEN_WIDTH - 4*BTN_WIDTH - SPACING_X)//4
startY = (INITIAL_PADDING_Y + SCREEN_HEIGHT - 4*FONT_SIZE - SPACING_Y)//4

Cancel = Button(w, text="C", font=("Aerial", FONT_SIZE), fg="red", width=BTN_WIDTH, command=lambda: appendValue(""))
Cancel.place_configure(x=startX, y=startY)

Brackets = Button(w, text="()", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("()"))
Brackets.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY)

Modulo = Button(w, text="%", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" % "))
Modulo.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY)

Divide = Button(w, text="/", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" / "))
Divide.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY)

# #row = 1
nine = Button(w, text="9", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("9"))
nine.place_configure(x=startX, y=startY + FONT_SIZE + SPACING_Y)

Eight = Button(w, text="8", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("8"))
Eight.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + FONT_SIZE + SPACING_Y)

Seven = Button(w, text="7", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("7"))
Seven.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + FONT_SIZE + SPACING_Y)

Multiply = Button(w, text="X", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" X "))
Multiply.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + FONT_SIZE + SPACING_Y)

# #row = 2
Six = Button(w, text="6", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("6"))
Six.place_configure(x=startX, y=startY + 2*(FONT_SIZE + SPACING_Y))

Five = Button(w, text="5", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("5"))
Five.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 2*(FONT_SIZE + SPACING_Y))

Four = Button(w, text="4", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("4"))
Four.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 2*(FONT_SIZE + SPACING_Y))

Subtract = Button(w, text="-", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" - "))
Subtract.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 2*(FONT_SIZE + SPACING_Y))

# #row = 3
Three = Button(w, text="3", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("3"))
Three.place_configure(x=startX, y=startY + 3*(FONT_SIZE + SPACING_Y))

Two = Button(w, text="2", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("2"))
Two.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 3*(FONT_SIZE + SPACING_Y))

One = Button(w, text="1", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("1"))
One.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 3*(FONT_SIZE + SPACING_Y))

Add = Button(w, text="+", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue(" + "))
Add.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 3*(FONT_SIZE + SPACING_Y))

# #row = 4
plusMinus = Button(w, text="+/-", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("-+"))
plusMinus.place_configure(x=startX, y=startY + 4*(FONT_SIZE + SPACING_Y))

Zero = Button(w, text="0", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("0"))
Zero.place_configure(x=startX + BTN_WIDTH + SPACING_X, y=startY + 4*(FONT_SIZE + SPACING_Y))

Point = Button(w, text=".", font=("Aerial", FONT_SIZE), width=BTN_WIDTH, command=lambda: appendValue("."))
Point.place_configure(x=startX + 2*(BTN_WIDTH + SPACING_X), y=startY + 4*(FONT_SIZE + SPACING_Y))

Equals = Button(w, text="=", font=("Aerial", FONT_SIZE),bg="green",fg="white", width=BTN_WIDTH, command=evaluate)
Equals.place_configure(x=startX + 3*(BTN_WIDTH + SPACING_X), y=startY + 4*(FONT_SIZE + SPACING_Y))

w.mainloop()