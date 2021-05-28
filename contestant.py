class Contestant:
    def __init__(self, first_name, last_name, email_address, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.registration_number = int(input("last four digits of phone number"))

    def notify_contestants(self, is_winner):
        if is_winner:
            print(f"Congratulations {self.first_name} {self.last_name}! You won the sweepstakes competition!!")
        else:
            print(f"{self.first_name} {self.last_name}, We're Sorry to inform that you "
                  f"did not win the sweepstakes competition.")
