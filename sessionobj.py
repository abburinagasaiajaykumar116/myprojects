#session object
from flask import Flask,render_template,request,session,redirect,url_for
app=Flask(__name__)
app.secret_key='ajay'
@app.route('/')
def index():
     if 'username' in session:
          username=session['username']
          return "<h3>you are logined in as "+username+"</h3><br>"+"<a href='\logout' >logout</a>"
     return "<h3>you are not logined </h3><br><a href='/login'>login</a>"
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
if __name__=="__main__":
    app.run()