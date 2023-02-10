from flask import   render_template, url_for, flash, redirect, session
from Authentication.forms import RegistrationForm, LoginForm
from Authentication.models import User
from Authentication import app, db,  bcrypt, login_manager
from flask_login import login_user

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/register", methods = ["POST", "GET"])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        info = User(username = form.username.data,  email = form.email.data, password = hashed_password )
        db.session.add(info)
        db.session.commit()
        
        flash('Compte cree avec succes', category = "success")
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)


@app.route("/login", methods = ["POST","GET"])
def  login():

    form =  LoginForm()
    if form.validate_on_submit():
         info = User.query.filter_by(email = form.email.data).first()
         if info and bcrypt.check_password_hash(info.password ,  form.password.data):
            
             return redirect(url_for('profile'))
         else:
             flash('Login Unsuccessful, check email and Password',  category = "error")
    return render_template('login.html', title = 'login', form=form)

@app.route("/profile", methods = ["POST","GET"])
def  profile():
    # data = session.get('data')
    return render_template("profile.html")

@app.route("/logout",  methods = ["POST","GET"] )
def logout():
    return redirect(url_for('login'))