from flask import Flask, request, render_template, redirect
import sqlite3

app=Flask(__name__)

SPORTS=['Cricket','Football','Basketball','Soceer']

@app.route('/',methods=['GET','POST'])
def main():
    if request.form.get('sport') and request.method=='POST':
        conn=sqlite3.connect('sports.db')
        c=conn.cursor()

        '''uncomment to first create a database and in reruns commnet it out'''
        # c.execute("create table register(name text)")
        c.execute('''INSERT INTO register(name) VALUES (?)''', (request.form.get('sport'),))
        conn.commit()

        c.execute('''SELECT name FROM register''')
        results=c.fetchall()
        print('registered sports',results)
        conn.close()
    return render_template('index.html',sports=SPORTS)

if __name__=="__main__":
    app.run(debug=True,port=5000)