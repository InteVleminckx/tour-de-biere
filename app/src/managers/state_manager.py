from enum import Enum


class HostStates(Enum):
    home_page = 0
    overview_page = 1
    etappe_page_not_started = 2
    etappe_page_started = 3


class UserStates(Enum):
    overview_page = 0
    etappe_page_not_started = 1
    etappe_page_started = 2
    finish_page = 3


class StateManager:

    def __init__(self):
        self.host_state = None

    def set_host_state(self, state):
        self.host_state = state
