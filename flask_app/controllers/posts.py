from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.post_model import Posts

@app.route('/user/create_post')
def create_post():
    # if "user_id" not in session:
    #     return redirect('/')
    return render_template('new-post.html')

@app.route('/user/submit_post', methods = ['POST'])
def validate_user_post():
    # if "user_id" not in session:
    #     return redirect('/')
    if not Posts.validate_post(request.form):
        return redirect('/user/create_post')
    data = {
        "user_id" : session['user_id'],
        "title" : session['title'],
        "text_content" : session['text_content'],
        "image" : session['image'],
    }
    Posts.create_post(data)
    return redirect('/user/dashboard')

@app.route('/post/edit/<int:id>')
def edit_post(id):
    # if "user_id" not in session:
    #     return redirect('/')
    posts = Posts.one_post({'id' : id})
    return render_template('edit_post.html', posts = posts)

@app.route('/post/edit/validation/<int:id>', methods=['POST'])
def validate_edit(id):
    # if 'user_id' not in session:
    #     return redirect('/')
    if not Posts.validate_post(request.form):
        return redirect(f'/posts/edit/{id}')
    data = {
        'id' :id,
        'title' : request.form['title'],
        'text_content' : request.form['text_content'],
        'image' : request.form['image']
    }
    Posts.update_post(data)
    return redirect('/user/dashboard')

@app.route('/post/delete/<int:id>')
def delete_one_post(id):
    # if 'user_id' not in session:
    #     return redirect('/')
    Posts.delete_post({'id' : id})
    return redirect('/user/dashboard')