from . import auth
from flask import render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user


from app.models import User
from app import db
from .forms import LoginForm

@auth.route('/login',methods=['GET','POST'])
def login():
    loginForm = LoginForm()

    if request.method == 'POST' and loginForm.validate_on_submit():
        email = loginForm.email.data
        password = loginForm.password.data
        # remember_me = loginForm.remember_me.data

        userlogin = User.query.filter_by(email=email).first()

        if userlogin is not None and userlogin.verify_password(password):
            # login_user(userlogin,remember_me)
            login_user(userlogin)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Usuario o password invalido','error')
       
    return render_template('login.html',form = loginForm)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesion','success')
    return redirect(url_for('main.index'))

