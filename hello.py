from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Napier?!!!RRRRRR"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world  :C"

@app.route("/private")
def private():
    #Test for user logged in failed
    #so redicted to login URL
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Now we would get username & password"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
