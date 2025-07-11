from flask import Flask
from flask_socketio import SocketIO
from config import Config

socketio = SocketIO(manage_session=True)

def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)

    from app.routes import discover_blueprints
    for bp in discover_blueprints():
        flask_app.register_blueprint(bp)

    import app.socket_events
    socketio.init_app(flask_app)

    return flask_app