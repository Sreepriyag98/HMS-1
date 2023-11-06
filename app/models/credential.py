from app.extensions import db
from flask_bcrypt import bcrypt
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import Flask
from datetime import datetime


class Credential(db.Model):
    paswrd_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def default_username(context):
            if context.get_current_parameters().get("user_id") is not None:
                user = User.query.get(context.get_current_parameters()["user_id"])
                if user:
                    return f"{user.first_name}@{user.dob}"
            return None

    username = db.Column(db.String(80), unique=True, nullable=False, default=default_username)
    password_hash = db.Column(db.String(60), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now)
    created_by=db.Column(db.String(64))
    updated_date = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)
    updated_by=db.Column(db.String(20))

    def _init_(self, user):
        self.user = user
        self.username = f"{user.first_name}@{user.dob.strftime('%Y%m%d')}"  # Combine name and dob in the format YYYY-MM-DD
        

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password,password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



    def __repr__(self):
        return f'<Question {self.user_id}>'