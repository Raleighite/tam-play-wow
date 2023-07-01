from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "No, Tam has not played WoW yet."

    """In May 2023 Tam promised his friends he would play World of Warcraft for 3 months starting at some point during the summer of 2023. This website tracks if Tam has played WoW yet, and reminds him of his commitment. 
    """
    
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', default=5000))
