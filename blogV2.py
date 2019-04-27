from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    number = 10
    manyFaces = {"Nick": "Nihil", "Learning": "Flask /w Python", "Road-map": "work-hard"}
    return render_template("index.html", number = number, manyFaces = manyFaces)


@app.route("/about")
def about():
    return "It's all about myself!"

if __name__ == "__main__":
    app.run(debug = True)