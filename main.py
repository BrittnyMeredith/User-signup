from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=["post"])
def correct_username(): 
    correct_email= request.form['email']
    correct_username = request.form['username']
    correct_password = request.form['password']
    verified_password = request.form['verify password']

    username_error = ""
    password_error = ""

    if correct_username == "" or len(correct_username) <3 or len(correct_username) >20: 
        username_error = "Please input a username between 3 and 20 characters"
    if " " in correct_username: 
        username_error = "Please input a username without spaces in between"
    if correct_password != verified_password:
        password_error="Passwords do not match"

    if username_error != "" or password_error != "":
        return redirect("/?password_error={}&username_error={}&correct_email={}&correct_username={}".format(password_error, username_error, correct_email, correct_username))

    return "Hello {username}, Welcome Back".format(username=correct_username)


@app.route("/")
def index():
    if request.args.get('username_error'):
        username_error = request.args.get('username_error')
    else: 
        username_error = ''
    if request.args.get('password_error'):
        password_error = request.args.get('password_error')
    else: 
        password_error= ''
    if request.args.get('correct_username'):
        correct_username=request.args.get('correct_username')
    else: 
        correct_username=''
    if  request.args.get('correct_email'):
        correct_email= request.args.get('correct_email')
    else: 
        correct_email=''
    return render_template('form.html', error=username_error, password_error=password_error, username=correct_username, email=correct_email)
app.run()