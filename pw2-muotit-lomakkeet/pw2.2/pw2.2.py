from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html", welcome_text="Tervetuloa Python kurssille!")

@app.route("/admin")
def admin():
    return render_template("admincp.html", name="Hello Thinh")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
