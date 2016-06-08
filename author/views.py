from flask_blog import app, db
from flask import render_template, redirect, url_for, session, request, flash
from author.form import RegisterForm
from author.form import LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    error = ''
    
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
    
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        author = Author.query.filter_by(
            username=form.username.data
            ).first()
        if author:
            if bcrypt.hashpw(form.password.data, author.password) == author.password:
                session['username'] = form.username.data
                session['is_author'] = author.is_author
                flash('User %s logged in' % form.username.data)
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('index'))
            else:
                error = 'Invalid username or passowrd'
        else:
            error = 'Invalid username or passowrd'
    return render_template('author/login.html', form=form, error=error)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)
    
@app.route('/success')
def success():
    return 'Author Registered!!!';
    
@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('is_author')
    flash('User logged out')
    return redirect('login')
    