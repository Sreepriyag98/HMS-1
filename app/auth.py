from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db  # Replace 'your_app' with your Flask app instance
from app.models.user import User  # Replace 'your_app.models' with your SQLAlchemy model
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))  # Assuming 'index' is the home page

        flash(error)

    return render_template('base.html')
