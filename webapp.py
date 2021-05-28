import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import threading

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"]

@app.route('/')
def timer():
    timer = threading.Timer(2.0, timer)
    timer.start()
def renderMain():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    session["answer1"] = request.form["answer1"]
    return render_template('page1.html')

@app.route('/submit1',methods=['POST'])
def submit1():
    session["answer2"] = request.form["answer2"]
    return render_template('page2.html')

@app.route('/submit2',methods=['POST'])
def submit2():
    session["answer3"] = request.form["answer3"]
    return render_template('page3.html')
@app.route('/restart')
def restart():
    return render_template('home.html')


def check():
    counter = 0
    if session["answer1"] == "A":
        counter = counter + 1
    if session["answer2"] == "B":
        counter = counter + 1
    if session["answer3"] == "C":
        counter = counter + 1
    if session["answer4"] == "D":
        counter = counter + 1
    return counter

@app.route('/submit3',methods=['POST'])
def submit3():
    session["answer4"] = request.form["answer4"]
    timer.cancel()
    return timer
    return render_template('page4.html', score = check())



if __name__=="__main__":
    app.run(debug=False)
