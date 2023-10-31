from app.extensions import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    gender = db.Column(db.String(100))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    addi_phone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    adhar_num = db.Column(db.String(20))
    DOB = db.Column(db.String(20))
    created_by = db.Column(db.String(20))
    updated_by = db.Column(db.String(20))
    created_date = db.Column(db.String(20))
    
    

    def __repr__(self):
        return f'<User "{self.title}">'()