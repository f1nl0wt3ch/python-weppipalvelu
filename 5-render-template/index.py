from flask import Flask, render_template

app = Flask('__name__')

@app.route("/")
def index(text="World!"):
    return render_template('base.html', text=text)

app.run(debug=True)
