from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get_genre_weights')
def get_genre_weights():
    return os.environ['FITROCKR_API_KEY']


if __name__ == '__main__':
    app.run()
