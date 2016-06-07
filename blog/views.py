from flask_blog import app
from flask import render_template, redirect, url_for, flash, session, abort
from blog.form import SetupForm, PostForm
from flask_blog import db
from author.models import Author
from blog.models import Blog, Category, Post
from author.decorators import login_required, author_required
import bcrypt
from slugify import slugify

POSTS_PER_PAGE = 3

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    blog = Blog.query.first()
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False) #False:show empty list if not exist, True: Show 404 page if not exist
    return render_template('blog/index.html', blog=blog, posts=posts)
    
@app.route('/admin')
@app.route('/admin/<int:page>')
@login_required
@author_required
def admin(page=1):
    if session.get('is_author'):
        posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
        return render_template('blog/admin.html', posts=posts)
    else:
        abort(403)
    
@app.route('/setup', methods=['GET','POST'])
def setup():
    form = SetupForm()
    error = ''
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
            )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
                )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = 'Error creating user'
        if author.id and blog.id:
            db.session.commit()
            flash('User and Blog Created')
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = 'Error creating blog'
        
            
    return render_template('blog/setup.html', form=form, error=error)
    
@app.route('/post', methods=['GET','POST'])
@author_required
def post():
    form = PostForm()
    error = ''
    if form.validate_on_submit():
        if form.new_category.data:
            new_category  = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            category = new_category
        elif form.category.data:
            category_id = form.category.get_pk(form.category.data)
            category = Category.query.filter_by(id=category_id).first()
        else:
            category = None
        blog = Blog.query.first()
        author = Author.query.filter_by(username=session['username']).first()
        slug = slugify(form.title.data)
        post = Post(
            blog,
            author,
            form.title.data,
            form.body.data,
            category,
            slug
            )
        db.session.add(post)
        db.session.flush()
        
        if post.id:
            db.session.commit()
            flash('Post Created')
            return redirect(url_for('article', slug=slug))
        else:
            db.session.rollback()
            error = 'Error creating post'
    return render_template('blog/post.html', form=form, error=error)
    
@app.route('/article/<slug>')
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/article.html', post=post)