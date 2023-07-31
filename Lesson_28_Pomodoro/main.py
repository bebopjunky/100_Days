from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")

    check.config(text="")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        title.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"), text="Work!")
    elif reps == 8:
        count_down(long_sec)
        title.config(bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"), text="Break!")
    else:
        count_down(short_sec)
        title.config(bg=YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"), text="Break!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    sec = count % 60
    min = count // 60
    if len(str(sec)) == 1:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

    mark = ""
    for _ in range(reps // 2):
        mark += "✓"
    check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title = Label(text="Timer")
title.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
check = Label()
btn_start = Button(text="Start", highlightthickness=0, command=start_timer)

btn_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

title.grid(column=2, row=1)
canvas.grid(column=2, row=2)
btn_start.grid(column=1, row=3)
check.grid(column=2, row=3)
btn_reset.grid(column=3, row=3)

window.mainloop()
