from flask import Flask, render_template, request
app = Flask("__name__")

class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password

def valid_login(user: User):
    if user.username == "admin" and user.password == "123456":
        return True
    else:
        return False

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        input = User(request.form['username'], request.form['password'])
        if valid_login(input):
            return render_template('login-form.html', welcome_text="Login is success.")
        else:
            error = 'Invalid username or password'
        return render_template('login-form.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
