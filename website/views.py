from django import views
from flask import Blueprint, render_template, flash


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template("login2.html")


@views.route('/home', methods=['GET', 'POST'])
def home():
    return "THIS is the home page"
