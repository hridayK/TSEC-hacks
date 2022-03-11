from django import views
from django.shortcuts import render
from flask import Blueprint, render_template, flash, redirect, url_for
from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from httpx import request
from .models import db, User, Note
# from github import Github


views = Blueprint('views', __name__)


# @views.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template("login2.html")


@views.route('/page_signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html", user=current_user)


@views.route('/homie', methods=['GET', 'POST'])
def homie():
    return render_template("app_web.html", user=current_user)

# @views.route('/home', methods=['GET', 'POST'])
# @login_required
# def home():
#     return render_template("home.html")


# @views.route('/home', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # username = current_user.username
    # g = Github()
    # user = g.get_user(username)
    # hreff = user.avatar_url
    return render_template("home.html", user=current_user)


@views.route('/explore', methods=['GET', 'POST'])
def exp():
    return render_template("profile_cards.html", user=current_user)
# @views.route('/frontback', methods=['GET', 'POST'])
# def frontback():
#     return render_template("frontback.html")


# @views.route('/backend', methods=['GET', 'POST'])
# def frontback():
#     return render_template("nc.html")


# @views.route('/web_dev', methods=['GET', 'POST'])
# @login_required
# def web():
#     return render_template("app_web.html")

# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     return render_template("home.html", User=current_user)

# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     return render_template("login2.html")
