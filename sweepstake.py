import contestant
from contestant import Contestant
from userinterface import *


class Sweepstake:
    def __init__(self, name):
        self.contestant = contestant
        self.name = name
        self.dictionary_of_contestants = {}
        registration_number = 1000

    def register_contestant(self, contestant):
        pass

    def pick_winner(self):
        pass

    def print_contestant_info(self):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
        print(contestant.registration_number)
