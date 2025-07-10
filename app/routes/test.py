from flask import Blueprint, render_template

test_bp = Blueprint('test', __name__, url_prefix='')

@test_bp.route('/')
def test():
    return render_template('index.html')