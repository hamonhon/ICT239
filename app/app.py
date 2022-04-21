from flask import Flask, render_template
from flask_login import login_required, current_user
from app import app, login_manager


@app.route('/base')
@app.route('/')
def show_base():
    return render_template('base.html')

@app.route('/packages')
def log():
    return render_template('packages.html', name=current_user.name, panel="Packages")

@app.route('/packages_q1admin')
def log():
    return render_template('packages.html', name="admin", panel="Packages")

@app.route('/packages_q1user')
def log():
    return render_template('packages.html', name="Hamon", panel="Packages")

@app.route("/upload", methods=['GET','POST'])
@login_required
def upload():
    # Not required to be implemented in Q1
    pass 