from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:BlogFun@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(500))
    entered = db.Column(Boolean)

    def __init__(self):
        self.title = title
        self.body = body
        self.entered = False

@app.route('/' methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        blog_title = request.form('title')
        blog_body = request.form('body')
        blog = Blog(blog_title, blog_body)
        db.session.add(blog)
        db.session.commit()

    blog_id = int(request.form['blog-id'])
    blog = Blog.query.get(blog_id)
    blog.entered = True
    db.session.add(blog)
    db.session.commit()

