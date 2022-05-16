from flask import render_template, redirect, session, request, flash 
from flask_app import app 
from flask_app.models.comment import Comment 
from flask_app.models.post import Post
from flask_app.models.user import User 



@app.route('/add/comment', methods =['POST'])
def add_comment(): 
    if 'user_id' not in session:
        return redirect('/logout')
    comment_data = {
        "content" : request.form["content"],
        "user_id" : session["user_id"],
        "post_id" : request.form["post_id"]
    }
    user_data = {
        "id": session ['user_id']
    }
    
    Comment.save(comment_data)
    return redirect ('/dashboard')
    # return render_template('dashboard.html', comment = Comment.post_with_comment(comment_data))


@app.route('/destroy/comment/<int:id>')
def destroy_comment(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Comment.destroy(data)
    return redirect('/dashboard')