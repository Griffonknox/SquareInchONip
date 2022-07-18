from app.main import bp
from flask import render_template, make_response, url_for, redirect

@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", nav_type="about_me")


@bp.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template("portfolio.html", nav_type="portfolio")


@bp.route('/work_experience', methods=['GET', 'POST'])
def work_experience():
    return render_template("work_experience.html", nav_type="work_experience")

@bp.route('/resume', methods=["GET", "POST"])
def resume():
    # binary_pdf = get_binary_pdf_data_from_database(id=id)
    # response = make_response(binary_pdf)
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'inline; filename=%ThompsonScott.pdf'
    # return response
    return redirect(url_for('static', filename='resume.pdf'))