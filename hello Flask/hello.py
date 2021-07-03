from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1><p>This is a paragraph.</p><img ' \
           'src="https://media.giphy.com/media/4EFs2Z5VPSthcfhwLn/source.gif" width=200> '


@app.route('/omi')
def omi():
    return 'OMU'


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
