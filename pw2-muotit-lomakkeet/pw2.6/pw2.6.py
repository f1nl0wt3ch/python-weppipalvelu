from flask import Flask, flash, request, url_for, redirect, render_template

app = Flask(__name__)
app.secret_key = "Z/+EQu9JSPlgrjbXVsRj4BSJ"
GENDERS = ["mies", "nainen"]

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        name=request.form["name"]
        gender=request.form["gender"]
        age=request.form["age"]
        if age.isnumeric() and int(age) >= 18:
            flash("Kiitos sinun palautteestasi!")
            return redirect(url_for('thankyou'))
        else:
            error = "Tietosi ei kelpaa."
    return render_template("index.html", genders=GENDERS, error=error)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
