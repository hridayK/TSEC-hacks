from django import views
from flask import Blueprint


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    return "THIS is the default page"


@views.route('/home', methods=['GET', 'POST'])
def home():
    return "THIS is the home page"
