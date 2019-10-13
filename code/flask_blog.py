from flask import Flask, render_template
from collections import namedtuple

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>hey mate, this is a change</h1>"

@app.route('/about')
def name():
    Person = namedtuple("Person", "name family")
    soroush = Person("soroush","khosravi")
    return  render_template("base.html", tuple=soroush)

if __name__ == "__main__":
    app.run(debug=True)




