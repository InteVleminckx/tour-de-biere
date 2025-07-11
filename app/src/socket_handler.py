from app.src.managers.state_manager import StateManager, HostStates, UserStates
from app.src.managers.user_manager import UserManager
from flask import request
from flask_socketio import emit


class SocketHandler:

    def __init__(self, socketio):
        self.setup_sockets(socketio)
        self.user_manager = UserManager()
        self.state_manager = StateManager()

    def setup_sockets(self, socketio):
        socketio.on_event('connect', self.on_connect)
        socketio.on_event('disconnect', self.on_disconnect)
        socketio.on_event('user_select', self.on_user_select)
        socketio.on_event('start', self.on_start)
        socketio.on_event('select_etappe', self.on_select_etappe)
        socketio.on_event('start_etappe', self.on_start_etappe)
        socketio.on_event('objective_complete', self.on_objective_complete)
        socketio.on_event('finish', self.on_finish)

    def on_connect(self):
        referrer = request.headers.get('Referer')

        if '0.0.0.0' in referrer:
           self.state_manager.set_host_state(HostStates.home_page)
           return

        print("Client connected")

    def on_disconnect(self):
        print(f"Client disconnected")

    def on_user_select(self, data):
        user_id = data['user_id']
        username = data['username']
        if not self.user_manager.get_user(user_id):
            self.user_manager.add_user(user_id, username)
            emit('user_added', {"data": username})
            self.user_manager.set_user_state(user_id, UserStates.overview_page)
            return

        # Todo: the user probably refreshed the page so already exists, notify user in which state he was

    def on_start(self):
        # Todo: change host and user state to overview page & notify users frontend to change
        pass

    def on_select_etappe(self, etappe_id):
        # Todo: change host and user state to overview page & notify to change to correct etappe
        pass

    def on_start_etappe(self):
        # Todo: start the timer, notify host to start timer in frontend and notify users frontend to set first button enabled
        pass

    def on_objective_complete(self, objective_id):
        # Todo: set user objective complete, make next one accessible, and update results table of host
        pass

    def on_finish(self):
        #Todo: notify host, user is finished and update results + stop timer for user. Change user page to finished
        # Also, host check if all users are done --> Notify host + users to change to overview page
        pass