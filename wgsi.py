from flask import Flask, render_template, request
from game import GameFlask

app = Flask(__name__)

@app.route('/')
def home():
    game = GameFlask()
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = GameFlask()
    game.grid = request.form['grid']
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)
