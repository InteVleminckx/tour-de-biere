
class User:

    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state