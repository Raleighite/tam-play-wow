from flask import Flask, jsonify
from flask_bootstrap import Bootstrap

import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return "Yes, Tam has played WoW, but, he hasn't leveled a character to 70 yet."

    """In May 2023 Tam promised his friends he would play World of Warcraft for 3 months starting at some point during the summer of 2023. This website tracks if Tam has played WoW yet, and reminds him of his commitment. 
    """
    
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', default=5000))
