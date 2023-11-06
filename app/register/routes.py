from flask import render_template, request, url_for, redirect
from app.register import bp
from app.extensions import db
from app.models.user import User
from app.models.credential import Credential



@bp.route('/register' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return redirect(url_for('register.index.html'))

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        DOB = request.form['DOB']
        phone = request.form['phone']
        addi_phone = request.form['addi_phone']
        address = request.form['address']
        email = request.form['email']
        adhar_num = request.form['adhar_num']
        password = request.form['password']
    

        
        
        
        user = User(first_name=first_name,last_name=last_name, gender=gender,DOB=DOB,phone=phone,addi_phone=addi_phone,address=address,email=email,adhar_num=adhar_num)
        credential = Credential(password=password)
        db.session.add(user)
        db.session.add(credential)
        db.session.commit()
        return redirect(url_for('register.index'))

