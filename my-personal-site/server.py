from flask import Flask, render_template

app = Flask(__name__)  # The name of current Directory, so it can RUN!!!


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
