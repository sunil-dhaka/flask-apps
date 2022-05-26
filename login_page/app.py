from flask import Flask, request, render_template, session, redirect
from flask_session import Session

# create app instance
app=Flask(__name__)

# define session configuration parameters
app.config['SESSION_PERMANENT']=False
app.config['SESSION_TYPE']='filesystem' # to store flask sessions on the harddrive 
Session(app) # to kind of link app with session(just intuitive sense)


@app.route('/')
def main():
    if not (session.get('username') and session.get('password')):
        return redirect('/login')
    return render_template('login.html')

# login page app route that handles both get and post requests
# if request is through get method then it renders the main index page
# otherwise checks for assigns session attributes to values from the html form
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username']=request.form.get('username')
        session['password']=request.form.get('password')
        return redirect('/')
    return render_template('index.html')

@app.route('/logout')
def logout():
    session['username']=None
    session['password']=None
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5000)