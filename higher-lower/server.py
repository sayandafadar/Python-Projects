from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1><img " \
           "src='https://media.giphy.com/media/4EFs2Z5VPSthcfhwLn/source.gif' 'width = 20'> "


random_number = random.randint(0, 9)
print(random_number)


@app.route("/<int:guess>")
def choose_number(guess):
    if guess > random_number:
        return "<h1 style='color:purple;'>Too High, Try Again!</h1><img " \
           "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'> "
    elif guess < random_number:
        return "<h1 style='color:tomato;'>Too Low, Try Again!</h1><img " \
           "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'> "
    else:
        return "<h1 style='color:teal;'>You found me!</h1><img " \
           "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'> "


if __name__ == "__main__":
    app.run(debug=True)
