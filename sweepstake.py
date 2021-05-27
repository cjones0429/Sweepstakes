from contestant import Contestant


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.dictionary_of_contestants = {}
        registration_number = 6100

    def register_contestant(self, contestant):
        pass

    def pick_winner(self):
        pass

    def print_contestant_info(self, contestant):
        print(self.contestant.first_name)
        print(self.contestant.last_name)
        print(self.contestant.email)
        print(self.contestant.registration_number)
