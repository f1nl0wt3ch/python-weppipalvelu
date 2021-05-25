from flask import Flask, render_template

app = Flask('__name__')
numbers = ["One", "Two", "Three"]
@app.route("/")
def index(text="World!"):
    return render_template('base.html', text=text)

@app.route("/for")
def get_numbers():
    return render_template('base.html', numbers=numbers)

app.run(debug=True, port=3000)
