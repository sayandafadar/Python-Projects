from flask import Flask, render_template
import datetime as dt
import requests

AGE_URL = f'https://api.agify.io?'
GENDER_URL = 'https://api.genderize.io?'

app = Flask(__name__)


@app.route('/')
def home():
    time_now = dt.datetime.now().year
    return render_template('index.html', time=time_now)


@app.route('/guess/<name>')
def age_gender(name):
    parameters = {
        "name": name,
    }
    age_response = requests.get(AGE_URL, params=parameters)
    age_response.raise_for_status()
    age_data = age_response.json()["age"]

    gender_response = requests.get(GENDER_URL, params=parameters)
    gender_response.raise_for_status()
    gender_data = gender_response.json()["gender"]
    return render_template('guess.html', name=name, age=age_data, gender=gender_data)


@app.route('/blog')
def blog():
    blog_url = ' https://api.npoint.io/5abcca6f4e39b4955965'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
