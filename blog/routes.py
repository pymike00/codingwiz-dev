from flask import render_template

from blog import app
from blog.models import Post


@app.route("/")
def homepage():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("homepage.html", posts=posts)


@app.route("/posts/<int:post_id>")
def post_detail(post_id):
    post_instance = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post_instance)


@app.route("/about")
def about():
    return render_template("about_page.html")