from flask import Flask, request, render_template

app = Flask(__name__)
def set_value_for_checkbox(request):
    if request.form.get("checkbox"):
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        checkbox = set_value_for_checkbox(request)
        return render_template("template.html", email=email, password=password, checkbox=checkbox)
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
