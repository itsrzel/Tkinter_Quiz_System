# Atlas Pinas - Philippine Geography Quiz
# Developed using Python Tkinter

import tkinter as tk
from tkinter import messagebox
import random
import os

# -------------------- QUIZ QUESTIONS --------------------
QUESTIONS = [
    {
        "question": "Which Philippine island is famous for its powdery white sand beaches, particularly White Beach?",
        "choices": ["A. Siargao", "B. Boracay", "C. Camiguin", "D. Coron"],
        "answer": "B"
    },
    {
        "question": "How many islands are there in total in the Philippines?",
        "choices": ["A. 7,107", "B. 7,641", "C. 7,500", "D. 8,000"],
        "answer": "B"
    },
    {
        "question": "What is the highest mountain in the Philippines?",
        "choices": ["A. Mount Mayon", "B. Mount Pulag", "C. Mount Kanlaon", "D. Mount Apo"],
        "answer": "D"
    },
    {
        "question": "Which Philippine province is home to the famous Mayon Volcano?",
        "choices": ["A. Albay", "B. Sorsogon", "C. Camarines Sur", "D. Quezon"],
        "answer": "A"
    },
    {
        "question": "What is the largest lake in the Philippines?",
        "choices": ["A. Taal Lake", "B. Lake Lanao", "C. Laguna de Bay", "D. Lake Sebu"],
        "answer": "C"
    },
    {
        "question": "Which Philippine province is known for the Banaue Rice Terraces?",
        "choices": ["A. Benguet", "B. Ifugao", "C. Mountain Province", "D. Kalinga"],
        "answer": "B"
    },
    {
        "question": "What is the longest mountain range in the Philippines?",
        "choices": ["A. Cordillera Central", "B. Zambales Mountains", "C. Sierra Madre", "D. Caraballo Mountains"],
        "answer": "C"
    },
    {
        "question": "Which province is famous for the Chocolate Hills?",
        "choices": ["A. Cebu", "B. Bohol", "C. Iloilo", "D. Negros Occidental"],
        "answer": "B"
    },
    {
        "question": "Which Philippine province is made up of islands located between Mindanao and the Zamboanga Peninsula?",
        "choices": ["A. Basilan", "B. Sulu", "C. Tawi-Tawi", "D. Dinagat Islands"],
        "answer": "D"
    },
    {
        "question": "Which island is home to the Puerto Princesa Underground River?",
        "choices": ["A. Mindanao", "B. Luzon", "C. Palawan", "D. Samar"],
        "answer": "C"
    }
]

# -------------------- APPLICATION SETTINGS --------------------
TIME_LIMIT = 15
HIGH_SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_score.txt")

BG = "#F3F7F5"
DARK = "#123B35"
GREEN = "#176B5B"
GOLD = "#E0AD45"
WHITE = "#FFFFFF"
MUTED = "#647873"
RED = "#C94C4C"
LIGHT_GREEN = "#E4F1EC"

root = tk.Tk()
root.title("Atlas Pinas | Philippine Geography Quiz")
root.geometry("820x700")
root.configure(bg=BG)
root.resizable(False, False)

# -------------------- QUIZ VARIABLES --------------------
quiz_questions = []
current_question = 0
score = 0
time_left = TIME_LIMIT
wrong_answers = []
timer_job = None
answered = False
selected_answer = tk.StringVar()

timer_label = None
feedback_label = None
submit_button = None
next_button = None
choice_buttons = []

# -------------------- HIGH SCORE FUNCTIONS --------------------
def get_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r", encoding="utf-8") as file:
                return int(file.read().strip())
        except (ValueError, OSError):
            return 0
    return 0


def save_high_score(new_score):
    if new_score > get_high_score():
        with open(HIGH_SCORE_FILE, "w", encoding="utf-8") as file:
            file.write(str(new_score))
        return True
    return False


# -------------------- GENERAL UI HELPERS --------------------
def clear_screen():
    for widget in main_frame.winfo_children():
        widget.destroy()


def make_header(subtitle="PHILIPPINE GEOGRAPHY QUIZ"):
    header = tk.Frame(main_frame, bg=DARK, height=105)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(header, text="ATLAS PINAS", font=("Georgia", 25, "bold"),
             bg=DARK, fg=WHITE).pack(pady=(17, 1))
    tk.Label(header, text=subtitle, font=("Arial", 9, "bold"),
             bg=DARK, fg="#D7E9E2").pack()


def get_choice_text(question, letter):
    for choice in question["choices"]:
        if choice.startswith(letter + "."):
            return choice
    return "No answer"


def styled_button(parent, text, command, bg=GREEN, fg=WHITE, width=18):
    return tk.Button(
        parent, text=text, command=command,
        font=("Arial", 11, "bold"), bg=bg, fg=fg,
        activebackground=GOLD, activeforeground=DARK,
        relief="flat", bd=0, cursor="hand2",
        width=width, pady=11
    )


# -------------------- START SCREEN --------------------
def show_start_screen():
    clear_screen()
    make_header("DISCOVER THE BEAUTY AND GEOGRAPHY OF THE PHILIPPINES")

    content = tk.Frame(main_frame, bg=BG)
    content.pack(fill="both", expand=True, padx=45, pady=28)

    tk.Label(content, text="Explore the 7,641 Islands",
             font=("Georgia", 23, "bold"), bg=BG, fg=DARK).pack(pady=(10, 8))
    tk.Label(content,
             text="Test what you know about the country's islands, mountains,\\nvolcanoes, lakes, provinces, and natural wonders.",
             font=("Arial", 11), bg=BG, fg=MUTED, justify="center").pack(pady=5)

    info = tk.Frame(content, bg=WHITE, highlightbackground="#DCE8E2", highlightthickness=1)
    info.pack(fill="x", pady=22, ipady=12)

    for title, value in [("QUESTIONS", "10"), ("TIME LIMIT", "15 seconds"), ("POINTS", "1 per correct answer")]:
        item = tk.Frame(info, bg=WHITE)
        item.pack(side="left", expand=True, padx=8, pady=8)
        tk.Label(item, text=value, font=("Arial", 14, "bold"), bg=WHITE, fg=GREEN).pack()
        tk.Label(item, text=title, font=("Arial", 8, "bold"), bg=WHITE, fg=MUTED).pack(pady=(3, 0))

    tk.Label(content, text=f"PERSONAL BEST:  {get_high_score()} / 10",
             font=("Arial", 12, "bold"), bg=BG, fg=GOLD).pack(pady=(2, 16))
    styled_button(content, "START EXPLORING", start_quiz, width=22).pack()
    tk.Label(content, text="Choose wisely. Your journey across the Philippines starts here!",
             font=("Arial", 9, "italic"), bg=BG, fg=MUTED).pack(pady=18)


# -------------------- START AND DISPLAY QUESTIONS --------------------
def start_quiz():
    global quiz_questions, current_question, score, wrong_answers
    stop_timer()
    quiz_questions = random.sample(QUESTIONS, len(QUESTIONS))
    current_question = 0
    score = 0
    wrong_answers = []
    show_question()


def show_question():
    global time_left, answered, timer_label, feedback_label
    global submit_button, next_button, choice_buttons

    clear_screen()
    answered = False
    selected_answer.set("")
    time_left = TIME_LIMIT
    question = quiz_questions[current_question]

    make_header("YOUR PHILIPPINE GEOGRAPHY CHALLENGE")

    body = tk.Frame(main_frame, bg=BG)
    body.pack(fill="both", expand=True, padx=42, pady=22)

    top = tk.Frame(body, bg=BG)
    top.pack(fill="x")
    tk.Label(top, text=f"QUESTION {current_question + 1} OF {len(quiz_questions)}",
             font=("Arial", 10, "bold"), bg=BG, fg=GREEN).pack(side="left")

    timer_label = tk.Label(top, text="", font=("Arial", 11, "bold"),
                           bg=LIGHT_GREEN, fg=DARK, padx=12, pady=6)
    timer_label.pack(side="right")

    # Progress bar made with Tkinter frames
    progress_bg = tk.Frame(body, bg="#DCE8E2", height=7)
    progress_bg.pack(fill="x", pady=(12, 22))
    progress_bg.pack_propagate(False)
    progress_fill = tk.Frame(progress_bg, bg=GOLD,
                             width=int(690 * (current_question + 1) / len(quiz_questions)))
    progress_fill.pack(side="left", fill="y")

    tk.Label(body, text=f"Current Score: {score} / 10",
             font=("Arial", 10, "bold"), bg=BG, fg=MUTED).pack(anchor="w")

    question_card = tk.Frame(body, bg=WHITE, highlightbackground="#DCE8E2", highlightthickness=1)
    question_card.pack(fill="x", pady=(13, 16), ipady=16)
    tk.Label(question_card, text=question["question"],
             font=("Arial", 15, "bold"), bg=WHITE, fg=DARK,
             wraplength=680, justify="left").pack(anchor="w", padx=22, pady=15)

    tk.Label(body, text="SELECT YOUR ANSWER", font=("Arial", 9, "bold"),
             bg=BG, fg=GREEN).pack(anchor="w", pady=(0, 8))

    choice_buttons = []
    for choice in question["choices"]:
        letter = choice[0]
        rb = tk.Radiobutton(
            body, text=choice, variable=selected_answer, value=letter,
            font=("Arial", 11), bg=WHITE, fg=DARK,
            activebackground=LIGHT_GREEN, selectcolor=LIGHT_GREEN,
            anchor="w", padx=15, pady=10, relief="flat",
            highlightthickness=1, highlightbackground="#DCE8E2",
            cursor="hand2"
        )
        rb.pack(fill="x", pady=4)
        choice_buttons.append(rb)

    feedback_label = tk.Label(body, text="", font=("Arial", 10, "bold"),
                              bg=BG, fg=GREEN, wraplength=690)
    feedback_label.pack(pady=(10, 4))

    buttons = tk.Frame(body, bg=BG)
    buttons.pack(pady=5)
    submit_button = styled_button(buttons, "SUBMIT ANSWER", submit_answer, width=17)
    submit_button.pack(side="left", padx=7)
    next_button = styled_button(buttons, "NEXT QUESTION  →", next_question, bg=GOLD, fg=DARK, width=17)
    next_button.pack(side="left", padx=7)
    next_button.config(state="disabled")

    update_timer()


# -------------------- TIMER --------------------
def update_timer():
    global time_left, timer_job
    if answered:
        return

    timer_label.config(
        text=f"TIME LEFT: {time_left}s",
        fg=RED if time_left <= 5 else DARK
    )

    if time_left == 0:
        time_up()
        return

    time_left -= 1
    timer_job = root.after(1000, update_timer)


def stop_timer():
    global timer_job
    if timer_job is not None:
        try:
            root.after_cancel(timer_job)
        except tk.TclError:
            pass
        timer_job = None


# -------------------- ANSWER CHECKING --------------------
def lock_choices():
    for button in choice_buttons:
        button.config(state="disabled")


def submit_answer():
    global score, answered

    if answered:
        return

    choice = selected_answer.get()
    if choice == "":
        messagebox.showwarning("No answer selected", "Please select an answer before submitting.")
        return

    answered = True
    stop_timer()
    lock_choices()
    submit_button.config(state="disabled")

    question = quiz_questions[current_question]
    if choice == question["answer"]:
        score += 1
        feedback_label.config(text="✓ Correct! Great job, explorer!", fg=GREEN)
    else:
        correct_text = get_choice_text(question, question["answer"])
        wrong_answers.append({
            "question": question["question"],
            "your_answer": get_choice_text(question, choice),
            "correct_answer": correct_text
        })
        feedback_label.config(text=f"✕ Not quite! The correct answer is {correct_text}.", fg=RED)

    next_button.config(state="normal")


def time_up():
    global answered
    if answered:
        return

    answered = True
    stop_timer()
    lock_choices()
    submit_button.config(state="disabled")

    question = quiz_questions[current_question]
    correct_text = get_choice_text(question, question["answer"])
    wrong_answers.append({
        "question": question["question"],
        "your_answer": "No answer (time is up)",
        "correct_answer": correct_text
    })
    feedback_label.config(text=f"⌛ Time is up! The correct answer is {correct_text}.", fg=RED)
    next_button.config(state="normal")


# -------------------- NEXT QUESTION --------------------
def next_question():
    global current_question
    if not answered:
        return

    current_question += 1
    if current_question < len(quiz_questions):
        show_question()
    else:
        show_results()


# -------------------- RESULTS AND ANSWER REVIEW --------------------
def show_results():
    clear_screen()
    total = len(quiz_questions)
    percentage = (score / total) * 100
    new_record = save_high_score(score)

    if percentage >= 90:
        message = "Outstanding! You are a Philippine geography expert!"
    elif percentage >= 70:
        message = "Great job! You know the Philippines well."
    elif percentage >= 50:
        message = "Good effort! Keep exploring and learning."
    else:
        message = "Every explorer starts somewhere. Try again!"

    make_header("YOUR JOURNEY HAS COME TO AN END")

    body = tk.Frame(main_frame, bg=BG)
    body.pack(fill="both", expand=True, padx=38, pady=16)

    tk.Label(body, text="QUIZ COMPLETED!",
             font=("Georgia", 22, "bold"), bg=BG, fg=DARK).pack(pady=(0, 5))
    tk.Label(body, text=f"{score} / {total}",
             font=("Arial", 29, "bold"), bg=BG, fg=GREEN).pack()
    tk.Label(body, text=f"{percentage:.0f}% CORRECT",
             font=("Arial", 11, "bold"), bg=BG, fg=GOLD).pack(pady=2)
    tk.Label(body, text=message, font=("Arial", 10),
             bg=BG, fg=MUTED, wraplength=700).pack(pady=(4, 8))

    record_text = "★ NEW PERSONAL BEST! ★" if new_record else f"PERSONAL BEST: {get_high_score()} / 10"
    tk.Label(body, text=record_text, font=("Arial", 10, "bold"),
             bg=BG, fg=GOLD).pack(pady=(0, 9))

    tk.Label(body, text="ANSWER REVIEW  |  INCORRECT ANSWERS",
             font=("Arial", 9, "bold"), bg=BG, fg=GREEN).pack(anchor="w", pady=(2, 5))

    review_frame = tk.Frame(body, bg=WHITE, highlightbackground="#DCE8E2", highlightthickness=1)
    review_frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(review_frame)
    scrollbar.pack(side="right", fill="y")
    review_box = tk.Text(review_frame, height=8, wrap="word",
                         font=("Arial", 9), bg=WHITE, fg=DARK,
                         relief="flat", padx=12, pady=8,
                         yscrollcommand=scrollbar.set)
    review_box.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=review_box.yview)

    if not wrong_answers:
        review_box.insert("end", "Perfect score! You answered all 10 questions correctly.")
    else:
        for number, item in enumerate(wrong_answers, start=1):
            review_box.insert("end", f"{number}. {item['question']}\n")
            review_box.insert("end", f"   Your answer: {item['your_answer']}\n")
            review_box.insert("end", f"   Correct answer: {item['correct_answer']}\n\n")
    review_box.config(state="disabled")

    buttons = tk.Frame(body, bg=BG)
    buttons.pack(pady=12)
    styled_button(buttons, "PLAY AGAIN", start_quiz, width=16).pack(side="left", padx=7)
    styled_button(buttons, "EXIT", on_close, bg=DARK, width=12).pack(side="left", padx=7)


def on_close():
    stop_timer()
    root.destroy()


# -------------------- RUN APPLICATION --------------------
main_frame = tk.Frame(root, bg=BG)
main_frame.pack(fill="both", expand=True)

root.protocol("WM_DELETE_WINDOW", on_close)
show_start_screen()
root.mainloop()
