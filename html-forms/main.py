from flask import Flask, render_template, request
import smtplib

EMAIL = 'dafadarts@gmail.com'
PASSWORD = 'a7U6+cbOc3+h7a'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=EMAIL, password=PASSWORD)
connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject:New User Message\n\n")


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)