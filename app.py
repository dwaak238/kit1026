from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('gamestart.html')

if __name__ == '__main__':
    app.run()
