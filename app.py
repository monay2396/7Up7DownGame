from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_bet = request.form['bet']
    result = random.choice(['Win', 'Lose'])
    return render_template('result.html', user_bet=user_bet, result=result)

if __name__ == '__main__':
    app.run(debug=True)
