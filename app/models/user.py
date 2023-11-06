from app.extensions import db
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    salutation = db.Column(db.String(20))
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    gender = db.Column(db.String(100))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    addi_phone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    adhar_num = db.Column(db.String(20))
    dob = db.Column(db.String(20))
    created_date = db.Column(db.DateTime, default=datetime.now)
    created_by=db.Column(db.String(64))
    updated_date = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)
    updated_by=db.Column(db.String(20))

    credential = db.relationship('Credential', backref='user')


    def __repr__(self):
        return f'<User {self.user_id}>'