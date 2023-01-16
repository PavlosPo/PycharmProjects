from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def create_headline():
    msg = "<h1>Guess a number between 0 and 9</h1>" \
          '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    return msg


def generate_colors():
    def wrapper(*args, **kwargs):
        color = random.choice([
            'AliceBlue',
            'Beige',
            'BlueViolet',
            'Brown',
            'Coral',
            'Crimson',
            'Cyan',
            'DarkGreen'])
        return f"<h1 color={color}" + args[0] + "</h1>"

    return wrapper


random_nummber = random.randint(1, 9)


@app.route("/<int:number_givven>")
# @generate_colors()
def game(number_givven):
    print(random_nummber)
    if number_givven == random_nummber:
        return "You Did it! You found me!!"
    elif number_givven < random_nummber:
        return "Too low!! Try Again!"
    elif number_givven > random_nummber:
        return "Too high!! Try Again"


create_headline()

if __name__ == "__main__":
    app.run(debug=True)
