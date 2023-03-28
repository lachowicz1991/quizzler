import tkinter as tk
from  quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizGUI():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = 0
        self.score_dis = tk.Label(text=str(self.score), background=THEME_COLOR, pady=20, padx=20, fg="white")
        self.score_dis.grid(row=0, column=1)

        self.card = tk.Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question = self.card.create_text(150, 125, font=("Arial", "20", "italic"), text='Some text', width=280)
        self.card.grid(row=1, column=0, columnspan=2)

        right_img = tk.PhotoImage(file="images/true.png")
        self.right = tk.Button(image=right_img, highlightthickness=0, command=self.click_right)
        self.right.grid(column=1, row=2, pady=50)

        wrong_img = tk.PhotoImage(file="images/false.png")
        self.wrong = tk.Button(image=wrong_img, highlightthickness=0, command=self.click_wrong)
        self.wrong.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.card.config(bg='white')
        if self.quiz.still_has_questions():
            self.card.config(bg='white')
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.question, text=q_text)
        else:
            self.card.itemconfig(self.question, text=f"GAME OVER \n Final Score:{self.score}")
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')



    def click_right(self):
        right =self.quiz.check_answer('True')
        self.give_feedback(right)

    def click_wrong(self):
        wrong = self.quiz.check_answer('False')
        self.give_feedback(wrong)

    def give_feedback(self, answer):
        if answer:
            self.card.config(bg='green')
            self.score += 1
            self.score_dis.config(text=str(self.score))
        else:
            self.card.config(bg='red')

        self.window.after(1000, self.get_next_question)