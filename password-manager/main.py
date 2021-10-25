from tkinter import *
import math




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)


# Canvas creation
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)


#  Website text and entry
website_label = Label(text='Website:')
website_entry = Entry(width=35)
website_label.grid(row=1 , column=0)
website_entry.grid(row=1, column=1, columnspan=2)


# Email/Username text and entry
username_label = Label(text='Email/Website:')
username_entry = Entry(width=35)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, columnspan=2)

# password text and entry and button
pass_label = Label(text='Password')
pass_entry = Entry(width=21)
pass_button = Button(text='Generate Password')
pass_label.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)
pass_button.grid(column=2, row=3)

# Add button
add_button = Button(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()