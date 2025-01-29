#Create a basic flask app that brings back your name
#push your work on git ensure there is a git ignore

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
       return "Navugga Deirdre Idah"

if __name__ == '__main__':
       app.run(debug=True)
