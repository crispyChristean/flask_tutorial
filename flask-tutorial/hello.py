from flask import flask

#Create an object using the Flask Class
app = Flask(__name__)

@app.route('/')
def hell():
    return 'Hello World'