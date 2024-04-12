#((P*(1+r)^n)-P)
from tkinter import Tk , Label, Entry, Button

CI = Tk()
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
PE = Entry(font=('Aerial', 20))
PE.place_configure(x=750, y=120)

#rate
RL = Label(CI, text='Enter the rate of interest : ',font=('Aerial', 20),width=25)
RL.place_configure(x = 200, y = 220)
RE = Entry(font=('Aerial', 20))
RE.place_configure(x = 750, y = 220)

#Time 
TL = Label(CI, text='Enter the time period : ',font=('Aerial', 20),width=25)
TL.place_configure(x=200, y=320)
TE = Entry(font=('Aerial', 20))
TE.place_configure(x = 750, y=320)

#button
Cal = Button(CI, text='CALCULATE !',font=('Aerial', 20),command=cal_CI)
Cal.place_configure(x = 570, y = 420)


CI.mainloop()