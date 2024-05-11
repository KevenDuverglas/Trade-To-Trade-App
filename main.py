from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session  # Import the Session module

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions on the filesystem
Session(app)

USER_CREDENTIALS = {'username': 'user', 'password': '1234'}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Login Attempt: ", username)
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['username'] = username
            print("Login Successful")
            return redirect(url_for('home'))
        else:
            print("Login Failed")
            return '<h1>Invalid username or password</h1>'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/items')
def items():
    if 'username' in session:
        return render_template('item_listing.html')
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile_page.html')
    return redirect(url_for('login'))

@app.route('/create')
def create():
    if 'username' in session:
        return render_template('create_post.html')
    return redirect(url_for('login'))

@app.route('/messages')
def messages():
    if 'username' in session:
        return render_template('messaging_interface.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
