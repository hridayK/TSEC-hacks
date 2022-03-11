import imp
from django.db import IntegrityError
from flask import Blueprint, render_template, flash, redirect, url_for, request, session
import requests
from flask_login import login_user, logout_user, login_required
from flask_login import current_user
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        if request.form.get('action1') == 'Login':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            # print(user.email)
            # print(user.password)
            # print(user.id)
            # print(user.username)
            # print(user.first_name)
            # user = User.query.all()
            # for i in user:
            #     print(i.first_name)
            #     print(i.email)
            #     print(i.password)
            #     print(i.id)
            #     print(i.username)
            #     print(i.g_link)
            if user:
                if check_password_hash(user.password, password):
                    flash(f"{user.first_name} has been logged In Succesfully!!",
                          category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                    # return render_template("home.html", User=current_user)
                else:
                    flash("Invalid Password", category='error')
        else:
            flash("Invalid Email! User does not exist", category='error')
        pass
    return render_template("login2.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/explore', methods=['GET', 'POST'])
def explore():
    return render_template("profile_cards.html")


@auth.route('/sign-up', methods=['POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        passwordc = request.form.get('passwordc')
        username = request.form.get('username')
        githublink = request.form.get('githublink')
        name = request.form.get('name')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category='error')
        elif len(password) < 6:
            flash("Password must be at least 6 characters", category='error')
        elif password != passwordc:
            flash("Passwords do not match", category='error')
        elif len(email) < 4:
            flash("Email must be at least 4 characters", category='error')
        elif len(username) < 2:
            flash("Username must be at least 2 characters", category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'),
                            username=username, g_link=githublink, first_name=name)
            db.session.add(new_user)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

            login_user(new_user, remember=True)
            flash("User created successfully", category='success')
            return redirect(url_for('auth.login'))

    return render_template("login2.html", user=current_user)
