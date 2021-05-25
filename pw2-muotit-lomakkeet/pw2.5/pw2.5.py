from flask import Flask, request, render_template

app = Flask(__name__)
CALS = [{"index": 1, "name": "kertaus"}, {"index": 2, "name": "jako"}, {"index": 3, "name": "plus"},
        {"index": 4, "name": "minus"}]

def calculate(selected_cal, one, two):
    if selected_cal == 1:
        return one * two
    elif selected_cal == 2:
        return one / two
    elif selected_cal == 3:
        return one + two
    else:
        return one - two

@app.route("/", methods=["GET", "POST"])
def login():
    result = None
    if request.method == "POST":
        one = request.form["number_one"]
        two = request.form["number_two"]
        cal = request.form.get("selected_cal")
        if one.isnumeric() and two.isnumeric():
            result = calculate(int(cal), int(one), int(two))
    return render_template("template.html", result=result, cals=CALS)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
