from flask import Flask

app = Flask(__name__)


@app.route("/")
def say_hello():
    msg = "<h1>Guess a number between 0 and 9</h1>" \
          '<img src="https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif">'
    return msg


say_hello()

if __name__ == "__main__":
    app.run(debug=True)
