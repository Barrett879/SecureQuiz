import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"]

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/submit',methods=['GET', 'POST'])
def submit():
    session["answer1"] = request.form["answer"]
    return render_template('page1.html')

@app.route('/submit1',methods=['GET', 'POST'])
def submit1():
    session["answer2"] = request.form["answer"]
    return render_template('page2.html')

@app.route('/submit2',methods=['GET', 'POST'])
def submit2():
    session["answer3"] = request.form["answer"]
    return render_template('page3.html')

@app.route('/check')
def check():
    counter = 0
    if session["answer1"] == "A":
        counter = counter + 1
    if session["answer2"] == "B":
        counter = counter + 1
    if session["answer3"] == "C":
        coutner = counter + 1
               
         

if __name__=="__main__":
    app.run(debug=True)
