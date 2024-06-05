import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.flashcards = []
        self.current_card = None
        self.score = 0
        self.total_questions = 0

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="Question", font=('Helvetica', 18))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=('Helvetica', 18))
        self.answer_entry.pack(pady=20)

        self.check_button = tk.Button(self.root, text="Check Answer", command=self.check_answer, font=('Helvetica', 18))
        self.check_button.pack(pady=20)

        self.next_button = tk.Button(self.root, text="Next Question", command=self.next_question, font=('Helvetica', 18))
        self.next_button.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Add Flashcard", command=self.add_flashcard, font=('Helvetica', 18))
        self.add_button.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0", font=('Helvetica', 18))
        self.score_label.pack(pady=20)

    def add_flashcard(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Flashcard")

        tk.Label(add_window, text="Question:", font=('Helvetica', 14)).pack(pady=10)
        question_entry = tk.Entry(add_window, font=('Helvetica', 14))
        question_entry.pack(pady=10)

        tk.Label(add_window, text="Answer:", font=('Helvetica', 14)).pack(pady=10)
        answer_entry = tk.Entry(add_window, font=('Helvetica', 14))
        answer_entry.pack(pady=10)

        def save_flashcard():
            question = question_entry.get()
            answer = answer_entry.get()
            if question and answer:
                self.flashcards.append((question, answer))
                messagebox.showinfo("Success", "Flashcard added!")
                add_window.destroy()
            else:
                messagebox.showwarning("Error", "Please enter both question and answer.")

        tk.Button(add_window, text="Save", command=save_flashcard, font=('Helvetica', 14)).pack(pady=20)

    def next_question(self):
        if not self.flashcards:
            messagebox.showwarning("No Flashcards", "Please add some flashcards first.")
            return

        self.current_card = random.choice(self.flashcards)
        self.question_label.config(text=self.current_card[0])
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        if not self.current_card:
            messagebox.showwarning("No Question", "Please click 'Next Question' to get a question.")
            return

        user_answer = self.answer_entry.get()
        correct_answer = self.current_card[1]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "Correct Answer!")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect! The correct answer was: {correct_answer}")

        self.total_questions += 1
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
