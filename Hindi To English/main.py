from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
word_data = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Hindi.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_word():
    global word_data, window_timer
    window.after_cancel(window_timer)
    word_data = random.choice(to_learn)
    new_french_word = word_data["Hindi"]
    canvas.itemconfig(title_text, text="Hindi", fill="black")
    canvas.itemconfig(word_text, text=new_french_word, fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    window_timer = window.after(5000, func=flip_card)


def flip_card():
    global word_data
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word_data["English"], fill="white")


def right_answer():
    to_learn.remove(word_data)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)
    new_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window_timer = window.after(5000, func=flip_card)
canvas = Canvas(width=800, height=526)

# Images
front_image = PhotoImage(file="images/card_front.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_answer)
right_button.grid(column=1, row=1)

new_word()
window.mainloop()
