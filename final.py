import csv
import tkinter as tk
import random

root = tk.Tk()

root.geometry("800x500")
root.title("Final")
root.resizable(width=False, height=False)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        
        self.title = tk.Label(root, text="")
        self.title.pack()

        self.button1 = tk.Button(root, text="", command=lambda:self.check_answer(self.button1))
        self.button1.pack()

        self.button2 = tk.Button(root, text="", command=lambda:self.check_answer(self.button2))
        self.button2.pack()

        self.button3 = tk.Button(root, text="", command=lambda:self.check_answer(self.button3))
        self.button3.pack()

        self.button4 = tk.Button(root, text="", command=lambda:self.check_answer(self.button4))
        self.button4.pack()

        self.update_question()

    def update_question(self):
        random.shuffle(self.questions[self.current_question][1:])
        self.title.config(text=self.questions[self.current_question][0])
        self.button1.config(text=self.questions[self.current_question][1])
        self.button2.config(text=self.questions[self.current_question][2])
        self.button3.config(text=self.questions[self.current_question][3])
        self.button4.config(text=self.questions[self.current_question][4])

    def check_answer(self, button):
        if button.cget("text") == self.questions[self.current_question][1]:
            self.score += 1
        self.current_question += 1
        if self.current_question == len(self.questions):
            self.show_result()
        else:
            self.update_question()

    def show_result(self):
        self.title.config(text="Your score is {}".format(self.score))
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()

questions = []
with open("questions.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter=",")
    for row in csvreader:
        questions.append(row)

quiz = Quiz(questions)

root.mainloop()
