from app.main import bp
from flask import render_template, request

@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@bp.route('/calculate', methods=['POST'])
def calculate():
    nip_dia = request.form["nipple"]
    print(nip_dia)
    return render_template("calculate.html")
