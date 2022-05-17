from flask import render_template, redirect, session, request, flash 
from flask_app import app 
from flask_app.models.profile import Profile 
from flask_app.models.user import User

@app.route('/new/profile')
def profile(): 
    if "user_id" not in session:
        return redirect ('/logout')
    data = { "id": session ['user_id']
    }
    return render_template("profile.html", user = User.get_by_id(data))


@app.route('/add/profile', methods =['POST'])
def add_profile(): 
    if 'user_id' not in session:
        return redirect('/logout')
    if not Profile.validate_profile(request.form): #check validation method 
        return redirect ('/new/profile')
    data = {
        "job_title" : request.form["job_title"],
        "about_me" : request.form["about_me"],
        "user_id" : session["user_id"], 
    }
    Profile.save(data)
    return redirect('/dashboard')


@app.route('/edit/profile/<int:id>')
def edit_profile(id): 

    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id": session ['user_id']
    }
    
    return render_template("edit_profile.html",edit = Profile.get_one(data), user=User.get_by_id(user_data))

@app.route('/update/profile/<int:id>', methods = ['POST'])
def update_profile(id): 
    print("************ /update/profile/<int:id>")
    if "user_id" not in session:
        return redirect ('logout')
    if not Profile.validate_profile(request.form):
        print('************, validation failed') 
        return redirect(f'/edit/profile/{id}')
    data = {
        "about_me": request.form["about_me"],
        "job_title": request.form["job_title"],
        "id":request.form["profile_id"]
    }
    print('************, data=', data)
    Profile.update(data)
    return redirect(f'/profile/{id}')

@app.route('/profile/<int:id>')
def show_profile(id): 

    if 'user_id' not in session:
        return redirect ('/logout')
    user_data = {
        "id": session ["user_id"]
    }
    profile_data = {
        "id": id 
    }

    return render_template("show_profile.html",  user = User.get_by_id(user_data), 
                        profile = Profile.get_one(profile_data))

@app.route('/destroy/profile/<int:id>')
def destroy_profile(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Profile.destroy(data)
    return redirect('/dashboard')