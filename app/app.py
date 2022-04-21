from flask import Flask, render_template
from flask_login import login_required, current_user
from app import app, login_manager

# Register Blueprint so we can factor routes
# from bmi import bmi, get_dict_from_csv, insert_reading_data_into_database
from auth import auth

# register blueprint from respective module
app.register_blueprint(auth)

# Importing other python files
from users import User

# Load the current user if any
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

@app.route('/base')
def show_base():
    return render_template('base.html')

@app.route('/packages')
def log():
    return render_template('packages.html', name=current_user.name, panel="Packages")

@app.route('/packages_q1admin')
def log_admin():
    return render_template('packages.html', name="admin", panel="Packages")

@app.route('/packages_q1user')
def log_user():
    return render_template('packages.html', name="Hamon", panel="Packages")

@app.route("/upload", methods=['GET','POST'])
@login_required
def upload():
    # Not required to be implemented in Q1
    pass 