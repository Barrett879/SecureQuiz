import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    session["answer1"] = request.form["answer"]
    return render_template('page1.html')


@app.route('/check')
def check():
    counter = 0
    if session["answer1"] == "A":
        counter = counter + 1
               
               
    
               

if __name__=="__main__":
    app.run(debug=False)
