from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


def api_brain(name_given):
    """
    It will return as a list
    the guessed Gender and Age of a given Name
    """
    genderize_endpoint = "https://api.genderize.io"
    agify_endpoint = 'https://api.agify.io'
    genderize_params = {
        'name': name_given,
        'country_id': 'GR'
    }
    agify_params = {
        'name': name_given,
        'country_id': 'GR'
    }
    response_gender = requests.get(url=genderize_endpoint, params=genderize_params)
    response_gender.raise_for_status()
    response_gender = response_gender.json()['gender']

    response_age = requests.get(url=agify_endpoint, params=agify_params)
    response_age.raise_for_status()
    response_age = response_age.json()['age']
    return [response_gender, response_age]


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    # **kwargs
    return render_template("index.html",
                           num=random_number,
                           year=current_year)


@app.route("/guess/<name>")
def guess(name):
    [gender, age] = api_brain(name)
    print(gender, age)
    return render_template("index.html",
                           name=name.capitalize(),
                           gender=gender.capitalize(),
                           age=age)


if __name__ == "__main__":
    app.run(debug=True)