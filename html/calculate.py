import pyrebase
from flask import *


config = {
             "apiKey": "AIzaSyDhZnTWGsoNOewmbrUewchz1iJ2Qp2Fn-k",
             "authDomain": "dam1-4afa7.firebaseapp.com",
             "databaseURL": "https://dam1-4afa7-default-rtdb.firebaseio.com",
             "projectId": "dam1-4afa7",
             "storageBucket": "dam1-4afa7.appspot.com",
             "messagingSenderId": "46587884710",
             "appId": "1:46587884710:web:2f233d202051cafeb4b067",
             "measurementId": "G-ETYFK80MJ4"
           }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)