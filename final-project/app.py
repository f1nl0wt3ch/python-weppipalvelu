from flask import Flask, Blueprint
from controllers.MainController import login, logout, show_blog
import os

views = os.path.abspath("views")
app = Flask("__name__", template_folder=views)

main_bp = Blueprint("main_bp", __name__)
main_bp.route('/', methods=['GET', "POST"])(login)
main_bp.route('/logout', methods=['POST'])(logout)
main_bp.route('/blog', methods=['GET'])(show_blog)
# main_bp.route('/<int:user_id>', methods=['GET'])(show)

app.register_blueprint(main_bp)
if __name__ == '__main__':
    app.run(debug=True)
