import contestant
import userinterface
from contestant import Contestant
from main import dictionary_of_contestants
from userinterface import *
import random
from main import *


class Sweepstake:
    def __init__(self, name):
        self.contestant = contestant
        self.name = name
        self.dictionary_of_contestants = {}
        self.registration_number = int

    # this is where you would be using dependency injection
    # you would turn the contestant info into a dictionary and add it to the dictionary
    # (working on that concept in main)
    def register_contestant(self, contestant):
        pass

    def pick_winner(self):
        random.choice(list(dictionary_of_contestants.values()))

    def print_contestant_info(self):
        print(userinterface.contestant_enter_firstname())
        print(userinterface.contestant_enter_lastname())
        print(userinterface.contestant_enter_email_address())
        print(userinterface.contestant_enter_registration_number())
