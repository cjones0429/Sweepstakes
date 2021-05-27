class Contestant:
    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = registration_number

    def notify(self, is_winner):
        if is_winner:
            pass
            (f"Congratulations {self.first_name} {self.last_name}! You won the sweepstakes competition!!")
        else:
            pass
            (f"{self.first_name} {self.last_name}, Sorry but you did not win the sweepstakes competition.")