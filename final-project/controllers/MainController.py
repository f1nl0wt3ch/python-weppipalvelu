from flask import Flask, session, redirect, url_for, request, render_template
import os

views = os.path.abspath("views")
app = Flask("__name__", template_folder=views)

# Login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]

        return render_template("login.html")
    else:
        if "userid" in session:
            return redirect(url_for("blog"))
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.pop('userid', None)
    return redirect(url_for('index'))

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

# Blog
@app.route("/blog", methods=["GET"])
def show_blog():
    if "userid" in session:
        return render_template("protected_folder/blog.html")
    return redirect(url_for("login"))
