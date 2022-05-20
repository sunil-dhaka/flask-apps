from crypt import methods
from flask import Flask, render_template, session, redirect, request
from flask_session import Session

app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]='filesystem'
Session(app)

@app.route('/')
def loggedIn():
    # if user is not logged in then also redirect to this page
    if not session.get("username"):
        return redirect('/login')
    return render_template('login_support.html')

@app.route('/login',methods=['GET','POST'])
def home():
    # if user is in session then let him access all logged in user features
    if request.method=='POST':
        session['username']=request.form.get('username')
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['username']=None
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5000)