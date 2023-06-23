from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "No, Tam has not played WoW yet."