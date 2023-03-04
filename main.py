import os
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        firstName = request.form['fname']
        lastName = request.form['lname']
        email = request.form['email']
        return redirect(url_for('chat', firstName=firstName, lastName=lastName, email=email, answer=""))
    elif request.method == 'GET':
        return render_template('home.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat(firstName, lastName, email, answer):
    if request.method == 'POST':
        if 'q1' in request.form:
            return render_template('chat.html', firstName=firstName, lastName=lastName, email=email, answer="Q1 Answer")
        elif 'q2' in request.form:
            return render_template('chat.html', firstName=firstName, lastName=lastName, email=email, answer="Q2 Answer")
        elif 'q3' in request.form:
            return render_template('chat.html', firstName=firstName, lastName=lastName, email=email, answer="Q3 Answer")
        elif 'q4' in request.form:
            return render_template('chat.html', firstName=firstName, lastName=lastName, email=email, answer="Q4 Answer")
        elif 'end' in request.form:
            return redirect(url_for('end', firstName=firstName, lastName=lastName, email=email))
        else:
            return render_template('chat.html', firstName="Error", lastName="Error", email="Error", answer="Error")

    elif request.method == 'GET':
        return render_template('chat.html', firstName=firstName, lastName=lastName, email=email, answer="Start")


if __name__ == '__main__':
    app.run()
