from flask import render_template
from app.register import bp

@bp.route('/')
def index():
    return render_template('register/index.html')