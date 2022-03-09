from flask import Blueprint, render_template, flash, redirect, url_for, request, session
import requests

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    print("login")
    if request.method == "POST":

        if request.form.get('action1') == 'Login':
            email = request.form.get('email')
            password = request.form.get('password')
            print(email, password)
            if email == 'mskasan30@gmail.com' and password == 'password':
                return "Login Successful"
            else:
                return "Login Failed"


# @auth.route('/#', methods=['GET', 'POST'])
