from flask import Flask, render_template
app = Flask(__name__)

posts=[
    {
        "author": "soroush",
        "title": "blig post 1",
        "content": "first content",
        "date": "18 october"
    },
    {
        "author": "farnaz",
        "title": "blig post 2",
        "content": "second content",
        "date": "20 october"
    }

]

@app.route('/home')
@app.route('/')
def hello():
    return render_template("home.html", posts=posts)

@app.route('/about')
def name():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)



