from .database import db
from .app import app 
from flask import Flask, render_template, request, redirect, url_for, session
from .models import User
import os

# this line here specifies the name of the folder where you want to transfer your picture
# folder should be part of your flask application
app.config["IMAGE_UPLOADS"] = 'static/images'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pass']
        images = request.files['avator']

        pic_name = images.filename

        # if images/'avator' not in request.files:
        #  not -> means no valiable in the varilable in this case user did not uplaod any picture
        if not images:
            # this code will inser/save the values in the table even if user did not upload a picture 
            # user only enterd values for username and password
            user = User(uname=uname, password=pwd,pic='0')

            try:
                db.session.add(user)
                db.session.commit()

                return redirect('/login')
            except:
                return 'Error'
        # request.files -> request.files is exist, if you want to use images you can write "images == True"
        elif uname == '' and pwd == '' and request.files:
            # picture uploaded will still be saved even if user did not enter username and password in the form
            user = User(uname='', password='',pic=pic_name)

            try:
                db.session.add(user)
                db.session.commit()

                return redirect('/login')
            except:
                return 'Error'
        else:
            # images.save(os.path.join(app.config["IMAGE_UPLOADS"], images.filename))
            # both are fine
            images.save(os.path.join(app.config["IMAGE_UPLOADS"], pic_name))


            user = User(uname=uname, password=pwd, pic=pic_name)

            try:
                db.session.add(user)
                db.session.commit()

                return redirect('/login')
            except:
                return 'Error'

            return redirect('/login')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(uname=request.form['username'], password=request.form['password']).first()
        
        if user:   
            session['id'] = user.id

            return redirect('/dashboard')
          
        else:  #False
            return 'Error in logging in'
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # if the variable id already excisted in the computer and the variable id has value already

    if 'id' in session:
        # get the id from session and pass it to python variable(user_id)
        user_id = session['id'] 

        user = User.query.filter_by(id=user_id).first()

        return render_template('dashboard.html', user=user)
    else:
        return 'Error'

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
