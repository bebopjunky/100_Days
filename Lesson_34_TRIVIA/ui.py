from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
HEIGHT = 300
WIDTH = 250


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUIZZY")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=WIDTH, height=HEIGHT)
        self.question_text = self.canvas.create_text(WIDTH / 2, HEIGHT / 2, width=250, text="Question goes here: ",
                                                     font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.score = Label()
        self.score.config(text=f"Score: ", pady=20, bg=THEME_COLOR, fg="white", font=("Arial", 14))
        self.score.grid(row=0, column=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true = Button(image=self.true_img, highlightthickness=0, pady=20, padx=20, command=self.check_true)
        self.true.grid(row=2, column=0)

        self.false = Button(image=self.false_img, highlightthickness=0, pady=20, padx=20, command=self.check_false)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text="End of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)
