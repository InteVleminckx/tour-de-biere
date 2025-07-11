from flask_socketio import emit
from app import socketio
from flask import request, session


@socketio.on('connect')
def handle_connect():

    print(f"Client connected", flush=True)
    emit('message', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print(f"Client disconnected", flush=True)

@socketio.on('select_user')
def select_user(data):
    if 'user_id' not in session:
        session['user_id'] = data['user_id']

    print(session, flush=True)
