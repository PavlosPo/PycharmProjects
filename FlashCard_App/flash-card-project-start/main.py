from tkinter import *
import numpy as np
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# import the data with words
df = pd.read_csv('data/french_words.csv')
df = df.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = np.random.choice(df)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

window = Tk()
# Window color and background
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)





# Canvas object inserts layer of items, overlaps items e.t.c.
canvas = Canvas(width=800, height=526)
# Image for front card
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img) # we need to insert it on the center coordinates
# Text for the canvas
card_title = canvas.create_text(400, 150, text= '', font=('Ariel', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text= '',font=('Ariel', 60, 'bold'), fill='black')
# Background color of image -- Remove in-perfections
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Position of front image
canvas.grid(row=0, column=0, columnspan=2) # columnspan: Starts at 0 but has 2 columns it total -- fixes the buttons

# Buttons
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)


next_card()



# Loops
window.mainloop()


