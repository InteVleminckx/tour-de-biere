from flask_socketio import emit, join_room, leave_room
from app import socketio

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('message', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('my_event')
def handle_my_event(json):
    print('Received json:', json)
    emit('my_response', json)
