# from tkinter import *
# import requests
#
#
# kanye_quote = ''
#
# def get_quote():
#     global kanye_quote, quote_text
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     kanye_quote = response.json()['quote']
#     canvas.itemconfig(quote_text, text=kanye_quote)
#
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()




import requests
import datetime as dt
MY_LAT = 37.983160
MY_LONG = 22.766100

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(data, '\n', sunrise, '\n', sunset)

time_now = dt.datetime.now()

print(time_now.hour)
