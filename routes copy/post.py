from turtle import title
from flask import Blueprint, request, render_template, redirect, url_for, request

post_pages = Blueprint("posts", __name__)

# @post_pages.get("/post/<string:title>")
# def displa_post(title:str):
#     return "Display post page."

@post_pages.route("/post/",methods = ["GET","POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        # Adding post to database here
        return redirect(url_for(".display_post",title=title))
    return render_template("new_post.html")

@post_pages.get("/post/<string:title>")
def display_post(title):
    content = "..." # How do we get the content?
    return render_template("post.html", title=title, content=content)

# @post_pages.get("/post/<string:title>")
# def display_post(title):
#     with Session(engine) as session:
#         statement = select(Post).where(Post.title == title)
#         post = session.exec(statement).first()
#         return render_template("post.html", title=title, content=post.content)