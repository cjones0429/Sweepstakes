def contestant_enter_firstname():
    first_name = input("Please enter your first name")
    return first_name


def contestant_enter_lastname():
    last_name = input("Please enter your last name")
    return last_name


def contestant_enter_email_address():
    email_address = input("Please enter a valid email address. This how we will notify you if you win.")
    return email_address


def contestant_enter_registration_number():
    registration_number = input("Please enter the last four digits of your phone number")
    return registration_number


def verify_contestant_info():
    user_verify_info = input("Is the information correct? yes or no")
    if user_verify_info == "yes":
        print("Thank you for your information.")
    else:
        contestant_enter_firstname()
        contestant_enter_lastname()
        contestant_enter_email_address()
        verify_contestant_info()


