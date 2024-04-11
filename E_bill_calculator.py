from tkinter import Tk , Label , Button , Entry

bill = Tk()
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
UE = Entry(font=('Verdana',25),width=15)
UE.place_configure(x=850 ,y=120)

Submit = Button(bill, text='SUBMIT' , font=('Verdana',23),command=calcu)
Submit.place_configure(x=650, y=230)

bill.mainloop()