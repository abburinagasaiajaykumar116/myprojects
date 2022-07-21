#message flashing
from flask import Flask,render_template,request,url_for,redirect,flash
app=Flask(__name__)
app.secret_key='ajay'
@app.route('/')
def index():
    return render_template('flashmessage.html')
@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=="POST":
       if request.form['username']!='admin' or request.form['password']!='admin':
           error='invalid credentials'
       else:
          flash('login successful')
          flash('logout before you login again')
          return redirect(url_for('index'))
    return render_template('login.html',error=error)
if __name__=='__main__':
    app.run()