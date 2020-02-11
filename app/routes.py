from flask import render_template, flash, redirect, request

from app import app

from app.login import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'João'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('modelo_index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        flash('Login solicitado por email {}, lembrar_me={}'.format(
            form.email.data, form.lembrar_me.data))
        return redirect('/index')
    return render_template('modelo_login.html', title='Sign In', form = form)