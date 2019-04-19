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

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect('/blog')

@app.route('/blog', methods=['POST', 'GET'])
def show_blogs():
    
    if request.args.get('id'):
        id = int(request.args.get('id'))
        blog = Blog.query.get(id)
        return render_template('individual_entry.html', blog = blog)

    blogs = Blog.query.all()
    
    return render_template('index.html', title="Blog", blogs=blogs)

@app.route('/newpost', methods=['POST', 'GET'])
def add_entry():
    error = ""
    if request.method == 'POST':
        blog_title = request.form['title']
        if not(blog_title):
            error = "Please enter a title for your blog post."
            return render_template('add_entry.html', title_error = error, title = blog_title)

        blog_body = request.form['body']
        if not(blog_body):
            error = "Please enter a body for your blog post."
            return render_template('add_entry.html', body_error = error, body = blog_body)
        else:

            blog = Blog(blog_title, blog_body)
            db.session.add(blog)
            db.session.commit()

            return redirect('/blog')
            
    return render_template('add_entry.html')   

if __name__ == '__main__':
    app.run()