from flask import Flask, render_template

app = Flask("__name__")
LANGUAGES = [{"i": 1, "text": "Python"}, {"i": 2, "text": "Java"}, {"i": 3, "text": "Javascript"}]

@app.route("/")
def index():
    return render_template("template.html", languages=LANGUAGES)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
