from tkinter import Tk, Frame, Button, Label

window = Tk()
window.title('Calci Hub')
window.state('zoomed')

heading = Label(window, text="Calci Hub", font=('Calibri', 30))
heading.grid(row=0, column=1)

sideBar = Frame(window, background="gray", width=window.winfo_width() - 1300, height=window.winfo_height(), borderwidth=5)
sideBar.grid(row=1, column=0)

B1 = Button(sideBar, text="simple calc", font=('Calibri', 20), borderwidth=10, )
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="simple calc", font=('Calibri', 20), borderwidth=10, )
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="simple calc", font=('Calibri', 20), borderwidth=10, )
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="simple calc", font=('Calibri', 20), borderwidth=10, )
B1.pack(pady=20,padx=10)
B1 = Button(sideBar, text="simple calc", font=('Calibri', 20), borderwidth=10, )
B1.pack(pady=20,padx=10)


window.mainloop()