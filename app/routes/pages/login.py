from flask import Blueprint, render_template

login_bp = Blueprint('select_user', __name__, url_prefix='')

@login_bp.route('/')
def qr_overview():
    return render_template('index.html')

@login_bp.route('/login')
def select_user():
    return render_template('login.html')
