from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def create_headline():
    msg = "<h1>Guess a number between 0 and 9</h1>" \
          '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    return msg


@app.route("/<int:number_given>")
def game(number_given):
    # print(random_nummber)
    # print(number_given)
    if number_given == random_nummber:
        return "<h1 style='color:green' >You Did it! You found me!!</h1>" \
               "<img src='https://media.giphy.com/media/dpSrm4cwUmCeQ/giphy.gif'>"
    elif number_given < int(random_nummber):
        return "<h1 style='color: red'>Too low!! Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/VeB9ieebylsaN5Jw8p/giphy.gif'>"
    elif number_given > int(random_nummber):
        return "<h1 style='color: purple'>Too high!! Try Again<h1>" \
               "<img src='https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif'>"
create_headline()

if __name__ == "__main__":
    random_nummber = random.randint(1, 9)
    app.run(debug=True)
