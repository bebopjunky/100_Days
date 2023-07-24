from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=200, height = 300)


def calc():
    km = 1.609344 * int(input.get())
    answer.config(text=str(f"{km} km"))

my_label = Label(text = "Enter Miles",font=("Courier",24))
my_label.grid(column=0,row=0)
input = Entry(width=20)
input.grid(column=0,row=1)
button = Button(width=20,text="submit",pady=10,command=calc)
button.grid(column=0,row=2)
answer = Label(font=("Courier",24))
answer.grid(column=0,row=3)



window.mainloop()

