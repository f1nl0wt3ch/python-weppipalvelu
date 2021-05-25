from flask import Flask, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DB_URI'] = "sqlite:///:memory:"
db = SQLAlchemy(app)

'''
CREATE TABLE blogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    createdDate DATETIME
);
'''
class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String(128), nullable=False)
    createdDate = db.Column(db.DateTime)

    def __init__(self, title, author, createdDate):
        self.title = title
        self.author = author
        self.createdDate = createdDate

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    blogs = Blog.query.all()
    return render_template("index.html", blogs=blogs)


@app.route("/create", methods=["POST"])
def create():
    title = request.form["title"]
    author = request.form["author"]
    createdDate = datetime.now()
    blog = Blog()
    blog.title = title
    blog.author = author
    blog.createdDate = createdDate
    blog.create()
    return redirect(url_for("index"))


@app.route("/edit", methods=["POST"])
def update():
    id = request.form["id"]
    blog = Blog.query.filter(id=id).one_or_none()
    if blog is not None:
        title = request.form["title"]
        author = request.form["author"]
        blog.title = title
        blog.author = author
        blog.createdDate = datetime.now()
        blog.update()
    return redirect(url_for("index"))


@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    blog = Blog.query.filter_by(id=id).one_or_none()
    if blog is not None:
        blog.delete()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
