from flask import Flask

app = Flask('__name__')

@app.route("/")
def index():
    return "Hei Thinh!"
app.run(port=2000)
#print(app)
