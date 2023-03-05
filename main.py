import os
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['firstName'] = request.form['fname']
        session['lastName'] = request.form['lname']
        session['email'] = request.form['email']
        return redirect(url_for('chat'))
    elif request.method == 'GET':
        return render_template('home.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        if request.form['q'] == "Does UC have a football team?":
            return render_template('chat.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'], answer="Yes, the Bearcats.")
        elif request.form['q'] == "Does UC have Computer Science Major?":
            return render_template('chat.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'], answer="UC does have a computer science major.")
        elif request.form['q'] == "Does UC have on campus housing?":
            return render_template('chat.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'], answer="They do have on campus housing.")
        elif request.form['q'] == "Do the dining halls have good food?":
            return render_template('chat.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'], answer="No...they do not.")
        elif request.form['q'] == "End":
            return redirect(url_for('end'))
        else:
            return render_template('chat.html', firstName="Error", lastName="Error", email="Error", answer="Error")

    elif request.method == 'GET':
        return render_template('chat.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'], answer="Start")


@app.route('/end', methods=['GET', 'POST'])
def end():
    return render_template('end.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
