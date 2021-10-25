from tkinter import *


def button_clicked():
    new_text = float(input.get())
    text4.config(text=f'{new_text * 1.609344}')


window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

#Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# Text1 
text1 = Label(text='Miles')
text1.grid(column=3, row=0)

# Text2
text2 = Label(text='is equal to ')
text2.grid(column=0, row=1)

# Text3
text3 = Label(text='Km')
text3.grid(column=3, row=1)

# Text4, shows the kilometers
text4 = Label(text='0')
text4.grid(column=2, row=1)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=0)


window.mainloop()