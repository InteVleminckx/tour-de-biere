from flask import session
from app.src.user import User

class UserManager:

    def __init__(self):
        self.users = {}

    def add_user(self, user_id, username):
        self.users[user_id] = User(username, user_id)
        session['user_id'] = user_id

    def remove_user(self, user_id):
        self.users.pop(user_id)
        session.pop('user_id')

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def set_user_state(self, user_id, state):
        self.users[user_id].set_state(state)

    def get_user_state(self, user_id):
        return self.users[user_id].get_state()