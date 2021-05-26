from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)

# This function always will be involked firstly
@app.before_first_request
def initMe():
    db.create_all()
    koira = Animal(name="Koira")
    kissa = Animal(name="Kissa")
    #db.session.add(koira)
    db.session.add_all([koira, kissa])
    db.session.commit()

@app.route("/")
def index():
    print(Animal.query.first().name)
    return render_template("index.html", animal=Animal.query.first(), animals=Animal.query.all())

if __name__ == "__main__":
    app.run(debug=True)
