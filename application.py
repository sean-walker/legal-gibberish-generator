'''
    application.py
    Sean Walker, Yale '19
    CPSC 185

    A basic Flask application.
'''

from flask import Flask, jsonify, render_template, request
from main import run_generator

# configure application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    num_words = int(request.args.get('num_words'))
    word = request.args.get('word')
    if not word or word == 'undefined':
        return run_generator(num_words)
    return run_generator(num_words, word)
