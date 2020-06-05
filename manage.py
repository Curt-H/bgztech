from flask import Flask, render_template
from config import app_config
from utils import log

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/happy')
def happy():
    return "Happy!"


def create_app():
    app = Flask(__name__)


if __name__ == '__main__':
    if app_config['host'] == '0.0.0.0' and app_config['debug']:
        log('Please check page at http://localhost')
    app.run(**app_config)
