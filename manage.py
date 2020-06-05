from flask import Flask, render_template
from config import app_config
from utils import log

app = Flask(__name__)


def create_app():
    app = Flask(__name__)

    from app.views import main as blueprint_main
    app.register_blueprint(blueprint_main)

    return app


if __name__ == '__main__':
    app = create_app() 

    if app_config['host'] == '0.0.0.0' and app_config['debug']:
        log('Please check page at http://localhost')
         
    app.run(**app_config)
