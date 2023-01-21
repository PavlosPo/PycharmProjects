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
    return render_template("guess.html",
                           name=name.capitalize(),
                           gender=gender.capitalize(),
                           age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html",
                           posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
