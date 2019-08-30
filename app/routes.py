from flask import url_for, render_template, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post


posts = [
    {
        'author': 'Januka Madushan',
        'title': 'Post 01',
        'content': 'Sample Post 01',
        'date_posted': 'August 28,2019'
    },
    {
        'author': 'Januka Madushan',
        'title': 'Post 02',
        'content': 'Sample Post 02',
        'date_posted': 'August 28,2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Register", form=form)

