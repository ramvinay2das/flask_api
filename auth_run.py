from flask import Flask, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

USER_DATA = {
    'admin':'adminpassword',
    'user':'userpassword'
}

@auth.verify_password
def verify_password(username, password):
    if not(username and password):
        return False
    return USER_DATA.get(username) == password

@app.route('/')
def home():
    return "Working demo"

@app.route('/private')
@auth.login_required
def get_private():
    return {"message":"accessed secured endpoint"}

if __name__ == "__main__":
    app.run(debug=True)
