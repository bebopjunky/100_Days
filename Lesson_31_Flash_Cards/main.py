import random
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "courier"
HEIGHT = 526
WIDTH = 800
timer = None
french = {}

# ---------------------------- LEARNT ------------------------------- #
def learnt():
    fr_en.remove(french)
    print(len(fr_en))

    data = pandas.DataFrame(fr_en)
    data.to_csv("data/french_words_to_learn.csv")

    new_word()

# ---------------------------- WORD GENERATOR ------------------------------- #
def new_word():
    global timer
    global french
    french = random.choice(fr_en)
    fr_word = french.get("French")
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=fr_word, fill="black")

    timer = window.after(3000, answer)


def answer():
    global french
    en_word = french.get("English")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=en_word, fill="white")
    canvas.itemconfig(card, image=card_back_image)

    window.after_cancel("timer")


# ---------------------------- LOAD ------------------------------- #
try:
    data = pandas.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

fr_en = data.to_dict(orient="records")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
canvas = Canvas(width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

card = canvas.create_image(WIDTH / 2, HEIGHT / 2, image=card_front_image)
wrong = Button(image=wrong_image, highlightthickness=0, command=new_word)
correct = Button(image=correct_image, highlightthickness=0, command=learnt)

wrong.config(bg=BACKGROUND_COLOR)
correct.config(bg=BACKGROUND_COLOR)

title = canvas.create_text(WIDTH / 2, HEIGHT / 2 - 100, text="Title", fill="black", font=(FONT_NAME, 28, "bold"))
word = canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Word", fill="black", font=(FONT_NAME, 36, "bold"))

canvas.grid(row=0, column=0, columnspan=3)

wrong.grid(row=2, column=0)
correct.grid(row=2, column=2)
new_word()
window.mainloop()
